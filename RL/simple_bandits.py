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
from lib.utils import EpsilonGreedyPolicy, Averages, GreedyPolicy, RandomPolicy

# Class to implement the Simple Bandit Agent Algorithm


class Bandit(object):

    def __init__(
        self,
        action_space_n=5,
        initial_values=None,
        policy=None,
        rewards=None
    ):

        # simple action space as vector
        self.actions = range(0, action_space_n)

        # Default to RandomPolicy
        self.policy = RandomPolicy() if not policy else policy

        # action value method (avm) = sample_average
        self.avm = Averages().sample_average

        n = len(self.actions)

        # Option to start from scratch or continue learning
        self.Q_init = np.zeros(n) if not initial_values else initial_values
        self.Q = np.copy(self.Q_init)

        # Action selected Count
        self.N = np.zeros(n)

        # State Action value record
        self.R = [[] for i in range(n)]

        # Rewards values used by the agent to calculate step-reward
        self.Rewards = np.array(np.random.randint(-5, 5, n) if not rewards else rewards)

        self.last_action = None

    def evaluate(self, action):
        return self.Rewards[action]

    def act(self):
        action = self.policy.select_action(self.Q, N=self.N)  # , t=self.t)
        self.last_action = action
        self.N[self.last_action] += 1

        return action

    def observe(self, reward):
        if self.R is not None:
            self.R[self.last_action].append(reward)

        if self.avm:
            self.avm(
                Q=self.Q,
                last_action=self.last_action,
                last_reward=reward,
                N=self.N
            )

    def summary(self):
        print(f'Actions: {["A-" + str(act) for act in self.actions]}')
        print(f'Rewards: {list(self.Rewards)}')        
        
        max_used_action_index = np.where(self.N == self.N.max())[0][0]
        max_used_action = "A-" + str(self.actions[max_used_action_index])
        max_reward_index = np.where(self.Rewards == self.Rewards.max())[0][0]
        max_reward_action = "A-" + str(self.actions[max_reward_index])
        
        print(f'Selected Actions N(a): {list(self.N)}')
        print(f'Max_Selected(a): {max_used_action}, Max_Reward(a):{max_reward_action}')
        print(f'Is Max_Reward Action Used Most: {max_used_action==max_reward_action}')
        print(f'Calculated Value Q(a): {list(self.Q)}')


if __name__ == "__main__":
    # Comparing the performance of various policies
    policies_to_evaluate = [
        RandomPolicy(),  # Select actions randomly each time
        GreedyPolicy(),  # Select actions with the highest reward each time
        # Select actions with the highest reward with P(1-epsilon)
        EpsilonGreedyPolicy(epsilon=0.01)
    ]

    for policy_to_use in policies_to_evaluate:
        
        # Using a Stationary Reward
        stationary_reward = [-1, -2, 5, -1, 3]
        training_epochs = 25  # Number of training epochs
        iterations = 100  # iterations per epoch
        avg_reward = 0  # start evaluation with 0

        agent = Bandit(
            rewards=stationary_reward,
            policy=policy_to_use
        )

        for j in range(training_epochs):
            for i in range(iterations):
                action = agent.act()
                reward = agent.evaluate(action)
                avg_reward += reward
                agent.observe(reward)

            avg_reward /= iterations

        print("#######################")
        print(f'using {policy_to_use.name()}')
        agent.summary()
        print(f'avg_reward: {avg_reward}')
