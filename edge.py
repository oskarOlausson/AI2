
from outNode import OutNode
from constants import Constants
import random

class Edge:
    def __init__(self, out, constants):
        self.learning_rate = constants.get_learning_rate()
        self.start_weight = 0 #(random.random() - 0.5) / 10000
        self.weight = self.start_weight
        self.out = out

    def get_weight(self):
        return self.weight

    def reset_weights(self):
        self.weight = self.start_weight

    def calculate_weight(self, input, facit):
        facit = self.out.get_correct(facit)

        error = facit - self.out.get_value()

        #fredriks
        #self.weight += self.learning_rate * error * input

        weight = (self.out.get_value() - facit) * self.out.get_value() * (1 - self.out.get_value()) * input

        self.weight -= (weight * self.learning_rate)

    def send_to_out(self, input):
        self.out.accumulate(self.weight * input)

