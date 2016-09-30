

class Constants():

    def __init__(self, learning_rate: object, start_weight: object) -> object:
        self.learning_rate = learning_rate
        self.start_weight = start_weight


    def get_learning_rate(self):
        return self.learning_rate

    def get_start_weight(self):
        return self.start_weight


