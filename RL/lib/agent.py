from lib.avm import SampleAverage
from lib.policy import RandomPolicy
import numpy as np

# Class to implement the Simple Bandit Agent Algorithm
class Bandit(object):

    def __init__(
        self,
        action_space_n=5,
        initial_values=None,
        policy=None,
        rewards=None,
        alpha=0.75,
        average_value_method=SampleAverage()
    ):

        # simple action space as vector
        self.actions = range(0, action_space_n)

        # Default to RandomPolicy
        self.policy = RandomPolicy() if policy is None else policy

        # action value method (avm) = sample_average
        self.avm = SampleAverage() if average_value_method is None else average_value_method

        n = len(self.actions)

        # Option to start from scratch or continue learning
        self.Q_init = np.zeros(n) if initial_values is None else initial_values
        self.Q = np.copy(self.Q_init)

        # Action selected Count
        self.N = np.zeros(n)

        # State Action value record
        self.R = [[] for i in range(n)]

        # Rewards values used by the agent to calculate step-reward
        self.Rewards = np.array(
            np.random.randint(-5, 5, n)) if rewards is None else rewards

        self.t = 0
        self.alpha = alpha

        self.last_action = None

    def evaluate(self, action):
        return self.Rewards[action]

    def act(self):
        action = self.policy.select_action(self.Q, N=self.N, t=self.t)
        self.last_action = action
        self.N[self.last_action] += 1
        self.t += 1

        return action

    def observe(self, reward):
        if self.R is not None:
            self.R[self.last_action].append(reward)

        if self.avm:
            self.avm.calculate(
                Q=self.Q,
                last_action=self.last_action,
                last_reward=reward,
                N=self.N,
                Q_init=self.Q_init,
                R=self.R,
                alpha=self.alpha
            )

    def summary(self):
        retVal = {}
        retVal['Actions'] = ["A-" + str(act) for act in self.actions]
        max_used_action_index = np.where(self.N == self.N.max())[0][0]
        max_used_action = "A-" + str(self.actions[max_used_action_index])

        # max_reward_index = np.where(self.Rewards == self.Rewards.max())[0][0]
        # max_reward_action = "A-" + str(self.actions[max_reward_index])

        retVal['N(a)'] = str(list(self.N))
        retVal['Max_Selected(a)'] = max_used_action        
        # print(f'Is Max_Reward Action Used Most: {max_used_action==max_reward_action}')
        # print(f'Reward History: {self.R[max_used_action_index]}')
        retVal['Q(a)'] = str(list(self.Q))

        return retVal
