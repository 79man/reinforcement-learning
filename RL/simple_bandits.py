# Simple Bandits Algorithm
# Initialize, for a = 1 to k:
#       Q(a) 0
#       N(a) 0
# Loop forever:
#  With Probability 1 - ϵ:
#       A = argmax-a(Q(a)), break ties randomly
#  else With Probability ϵ:
#       A = a random action
# R  = bandit(A)
# N(A) = N(A) + 1
# Q(A) = Q(A) + 1/N(A)(R − Q(A))
#
import numpy as np
from lib.policy import EpsilonGreedyPolicy, GreedyPolicy, RandomPolicy, UpperConfidenceBoundPolicy
from lib.avm import SampleAverage, ExponentialRecencyWeightedAverage
from lib.agent import Bandit

from matplotlib import pyplot as plt
import math
from datetime import datetime # for time elapsed calculation
from progress.bar import Bar


def main():
    # Hyperparameters
    action_space_n = 10

    # Selecting the average Value Creation method from [SampleAverage, ExponentialRecencyWeightedAverage]
    avg_val_method = SampleAverage()#ExponentialRecencyWeightedAverage()

    # For each policy run the simulation for X epochs with Y iterations each
    training_epochs = 100  # Number of training epochs
    iterations = 100  # iterations per epoch

    # Number of times to execute the whole trial
    Num_retrials = 6
    Num_cols = 2
    Num_rows = math.ceil(Num_retrials/Num_cols)

    # Comparing the performance of various policies
    policies_to_evaluate = [
        # RandomPolicy(),  # Select actions randomly each time
        GreedyPolicy(),  # Select actions with the highest reward each time        
        EpsilonGreedyPolicy(epsilon=0.01), # Select actions with the highest reward with P(1-epsilon)
        EpsilonGreedyPolicy(epsilon=0.1), # Select actions with the highest reward with P(1-epsilon)
        UpperConfidenceBoundPolicy()
    ]

    fig, axs = plt.subplots(
        nrows=Num_rows,
        ncols=Num_cols,
        sharex=True,
        # sharey=True
    )

    for r_axis in range(Num_rows):
        for c_axis in range(Num_cols):
            # Using a Stationary Reward for each evaluation cycle
            # stationary_reward = np.array([-1, -2, -5, -1, 6, 2, -3, 4, 0, 1])
            stationary_reward = np.random.normal(0, 5, size=action_space_n).astype(int)

            for policy_to_use in policies_to_evaluate:
                curr_record = {}
                avg_reward = 0  # start evaluation with 0

                np.random.seed()

                N_arm_bandit = Bandit(
                    rewards=stationary_reward,
                    policy=policy_to_use,
                    average_value_method=avg_val_method,
                    action_space_n=action_space_n
                )

                curr_record['policy'] = policy_to_use.name()
                curr_record['avm'] = avg_val_method.name()
                curr_record['rewards'] = str(stationary_reward)
                curr_record['best_reward'] = stationary_reward.max()
                curr_record['best_action'] = "A-" + \
                    str(np.where(stationary_reward ==
                        stationary_reward.max())[0][0])
                
                # print(f'rewards: {stationary_reward}')
                # print(f'Best Reward: {stationary_reward.max()}, Best Action:{"A-" + str(np.where(stationary_reward == stationary_reward.max())[0][0])}')
                # print(curr_record)

                # records start time
                start_time = datetime.now()

                curr_record['data'] = {'iter': [], 'values': []}
                with Bar('Processing ' + policy_to_use.name() + " " + avg_val_method.name() + " ",max = training_epochs) as bar:
                    for j in range(training_epochs):
                        for i in range(iterations):
                            action = N_arm_bandit.act()
                            reward = N_arm_bandit.evaluate(action)
                            avg_reward += reward
                            N_arm_bandit.observe(reward)

                        avg_reward /= iterations
                        # print(f'iter: {j*iterations}, avg_reward: {avg_reward}')
                        curr_record['data']['iter'].append(j*iterations)
                        curr_record['data']['values'].append(avg_reward)
                        # print(curr_record)
                        bar.next()

                # records end time
                end_time = datetime.now()

                curr_record['training_iterations'] = training_epochs * iterations
                curr_record['time_elapsed'] = (end_time - start_time).total_seconds()
                curr_record['summary'] = N_arm_bandit.summary()
                print(f'{curr_record}')                
                
                # Scatter plotting the learning curve
                legend_lbl = ""
                if r_axis > 0 or c_axis > 0:
                    legend_lbl = "_"  # Avoid labels for each iteration

                legend_lbl = legend_lbl + policy_to_use.name()

                axs[r_axis][c_axis].plot(
                    np.array(curr_record['data']['iter']),
                    np.array(curr_record['data']['values']),
                    label=legend_lbl
                )
            
            # Common reward table for all the polices
            the_table = axs[r_axis][c_axis].table(
                cellText=[[rew for rew in list(stationary_reward)]],
                rowLabels=[f'Iter # {r_axis*Num_cols + c_axis}: Rewards'],
                loc='top',
                rowLoc='center',
                colLoc='center'                
            )

    for ax in axs.flat:
        ax.set(xlabel='Iterations', ylabel='Average Reward')
    plt.xlabel("Iterations")
    plt.ylabel("Average Reward")
    # plt.legend(
    #     # bbox_to_anchor =(0.75, 1.15),
    #     loc="center right",
    #    borderaxespad=0.1
    # )
    plt.figlegend(loc='lower center', ncol=5, labelspacing=0.)
    fig.suptitle("RL Algo learning curve")
    # plt.subplots_adjust(top=0.01)
    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
