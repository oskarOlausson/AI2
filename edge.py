

class Edge:
    """
        Gives information from the input (the pixels) and sends it to the output
    """
    def __init__(self, out, constants):
        self.learning_rate = constants.get_learning_rate()
        self.start_weight = 0
        self.weight = self.start_weight
        self.out = out

    def get_weight(self):
        """
        Returns the current weight (how much it contributes to the answer)
        """
        return self.weight

    def reset_weights(self):
        self.weight = self.start_weight

    def calculate_weight(self, input, facit):
        """
        Recalculates the input so the answer will come closer to the facit
        """
        facit = self.out.get_correct(facit)
        weight = (self.out.get_value() - facit) * self.out.get_value() * (1 - self.out.get_value()) * input
        self.weight -= (weight * self.learning_rate)

    def send_to_out(self, input):
        self.out.accumulate(self.weight * input)

