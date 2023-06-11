# Abstract Base class for Average Value Methods(AVM)
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
