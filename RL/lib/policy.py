import math
import numpy as np

class Policy(object):

    def __init__(self, name="Abstract Policy"):
        self._name = name

    def select_action(self, Q, **kwargs):
        pass

    def name(self):
        return self._name


class RandomPolicy(Policy):

    def __init__(self, name="Random Policy"):
        super(RandomPolicy, self).__init__(name)

    def select_action(self, Q, **kwargs):
        n = len(Q)
        return np.random.randint(n)


class GreedyPolicy(Policy):

    def __init__(self, name="Greedy Policy"):
        super(GreedyPolicy, self).__init__(name)

    def select_action(self, Q, **kwargs):
        argmax_list = np.flatnonzero(Q == Q.max())
        return np.random.choice(argmax_list)


class EpsilonGreedyPolicy(Policy):

    def __init__(self, epsilon=0.1):
        name = "Epsilon Greedy Policy(" + str(epsilon) + ")"
        super().__init__(name)

        self.epsilon = epsilon
        self.rp = RandomPolicy()
        self.gp = GreedyPolicy()

    def select_action(self, Q, **kwargs):
        sample_prob = np.random.uniform()

        if sample_prob < self.epsilon:
            return self.rp.select_action(Q)
        else:
            return self.gp.select_action(Q)


class UpperConfidenceBoundPolicy(Policy):

    def __init__(self, c=1):
        self.c = c
        name = "UCB Policy"
        super().__init__(name)

    def select_action(self, Q, N, t):

        ucb = np.array(
            [
                self.__ucb__(action, q_action, N, t)
                for action, q_action in np.ndenumerate(Q)
            ]
        )
        action = np.random.choice(np.flatnonzero(ucb == ucb.max()))
        return action

    def __ucb__(self, action, q_action, N, t):
        if N[action] == 0:
            return float('inf')
        else:
            return q_action + self.c * math.sqrt(math.log(t) / N[action])
