
from math import exp

class OutNode:
    def __init__(self, goal_value, is_eyes):
        self.reset_value()
        self.goal_value = goal_value
        self.is_eyes = is_eyes

    def get_goal_value(self):
        return self.goal_value

    def get_value(self):
        return self.out_value

    def reset_value(self):
        self.out_value = 0

    def accumulate(self, edge_value):
        self.out_value += edge_value

    def is_it_eyes(self):
        return self.is_eyes

    def get_correct(self, facit):
        if self.is_eyes:
            return self._get_correct_eyes(facit)
        else:
            return self._get_correct_mouth(facit)

    def _get_correct_eyes(self, facit):
        if facit <= 2:
            return self.goal_value == 1
        else:
            return self.goal_value == 2

    def _get_correct_mouth(self, facit):
        if facit == 1 or facit == 3:
            return self.goal_value == 1
        else:
            return self.goal_value == 2

    def get_error(self, facit):
        facit = self.get_correct(facit)
        return abs(self.get_value() - facit)

    def process_out_value(self):
        self.out_value = 1 / (1 + exp(-self.out_value))
        return self.out_value
