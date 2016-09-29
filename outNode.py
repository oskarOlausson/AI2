

class OutNode:
    def __init__(self, goal_value):
        self.current_value = 0
        self.goal_value = goal_value

    def get_goal_value(self):
        return self.goal_value

    def get_value(self):
        return self.out_value

    def set_value(self, out_value):
        self.out_value = out_value
