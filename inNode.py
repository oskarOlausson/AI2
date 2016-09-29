from edge import Edge
from constants import Constants

class InNode:

    def __init__(self, pixel, output_list, constants):
        self.pixel = pixel

        self.edges = list()
        for output in output_list:
            self.edges.append(Edge(output, constants))

    def update_pixel(self, pixel):
        self.pixel = pixel

    def reset_weights(self):
        for edge in self.edges:
            edge.reset_weight()

    def calculate_weights(self, facit):
        for edge in self.edges:
            edge.calculate_weight(self, facit)


