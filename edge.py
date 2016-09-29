
from outNode import OutNode
from constants import Constants

class Edge:
    def __init__(self, out, constants):
        self.learning_rate = constants.get_learning_rate()
        self.start_weight = constants.get_start_weight
        self.weight = self.start_weight
        self.out = out

    def get_weight(self):
        return self.weight

    def reset_weights(self):
        self.weight = self.start_weight

    def calculate_weight(self, input, facit):
        if self.out.get_goal_value() == facit: facit = 1
        else: facit = 0

        weight = (self.out.get_value() - facit) * self.out.get_value() * (1 - self.out.get_value()) * input
        self.weight -= (weight * self.learning_rate)

