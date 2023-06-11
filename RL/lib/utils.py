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

# Abstract Base class
class Average(object):

    def calculate(self, **kwargs):
        pass

    def name(self):
        return "Abstract Average"

class SampleAverage(Average):

    # Qn+1 =  Qn + (1/n)[(Rn - Qn)]
    def calculate(
            self,         
            Q,
            last_action,
            last_reward,
            N,
            **kwargs
    ):
        Q[last_action] += (last_reward - Q[last_action]) / N[last_action]

    def name(self):
        return "Sample Average"
    
class ExponentialRecencyWeightedAverage(Average):
    #               n
    # (1-α)^n Q1 +  Σ  α(1 − α)^(n−i) Ri
    #              i=1
    def calculate(
            self,
            Q,
            last_action,
            last_reward,
            Q_init,
            R,
            alpha,
            **kwargs
    ):
        n = len(R[last_action])
        
        Q[last_action] = pow(1 - alpha, n) * Q_init[last_action]
        
        for i in range(1, n):
            Q[last_action] += alpha * pow(1 - alpha, n - i) * R[last_action][i]

    def name(self):
        return "Exponential Recency Weighted Average"
