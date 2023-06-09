import math
import numpy as np

class Policy(object):

    def select_action(self, Q, **kwargs):
        pass

    def name(self):
        return "Abstract Policy"

class RandomPolicy(Policy):

    def select_action(self, Q, **kwargs):
        n = len(Q)
        return np.random.randint(n)
    
    def name(self):
        return "Random Policy"

class GreedyPolicy(Policy):

    def select_action(self, Q, **kwargs):
        argmax_list = np.flatnonzero( Q == Q.max() )
        return np.random.choice( argmax_list )
    
    def name(self):
        return "Greedy Policy"

class EpsilonGreedyPolicy(Policy):

    def __init__(self, epsilon=0.1):
        self.epsilon = epsilon
        self.rp = RandomPolicy()
        self.gp = GreedyPolicy()

    def select_action(self, Q, **kwargs):
        sample_prob = np.random.uniform()

        if sample_prob < self.epsilon:
            return self.rp.select_action(Q)
        else:
            return self.gp.select_action(Q)
        
    def name(self):
        return "Epsilon Greedy Policy"
        
class Averages(object):

    # Qn+1 =  Qn + (Rn - Qn)/n
    def sample_average(self, Q, last_action, last_reward, N):
        Q[last_action] += (last_reward - Q[last_action]) / N[last_action]