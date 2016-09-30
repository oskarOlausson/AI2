
from math import exp

class OutNode:
    def __init__(self, goal_value):
        self.reset_value()
        self.goal_value = goal_value

    def get_goal_value(self):
        return self.goal_value

    def get_value(self):
        return self.out_value

    def reset_value(self):
        self.out_value = 1

    def accumulate(self, edge_value):
        self.out_value *= edge_value

    def process_out_value(self):
        self.out_value = 1 / (1 + exp(-self.out_value))
        return self.out_value
