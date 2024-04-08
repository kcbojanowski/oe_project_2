import numpy as np

class FitnessFunction:
    def compute(self, x):
        raise NotImplementedError("Subclasses must implement this method")

class MartinAndGaddyFunction(FitnessFunction):
    def compute(self, x):
        term1 = (x[0] - x[1])**2
        term2 = (x[0] + x[1] - 10)**2 / 3
        return term1 + term2

class AckleyFunction(FitnessFunction):
    def __init__(self, D = 2):
        self.D = D  # Dimensions
    
    def compute(self, x):
        sum_sq = np.sum(x**2)
        sum_cos = np.sum(np.cos(2 * np.pi * x))
        term1 = -20 * np.exp(-0.2 * np.sqrt(sum_sq / self.D))
        term2 = -np.exp(sum_cos / self.D)
        return term1 + term2 + 20 + np.e