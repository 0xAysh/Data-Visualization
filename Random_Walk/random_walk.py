from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        #All walks starts at 0
        self.x_value = [0]
        self.y_value = [0]

    def get_step(self):
        """chooses Direction and distance and calculates and return steps"""
        direction = choice([1, -2])
        distance = choice([0, 1, 2, 3, 4])
        steps = direction * distance

        return steps

    def fill_walk(self):
        """Calculate all the points in the walk."""

        #Keep taking steps until the walks reaches desire length.
        while len(self.x_value) < self.num_points:

            #Decide which direction to go and how to go.
            x_step = self.get_step()
            y_step = self.get_step()

            #Rejects move that goes nowhere.
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position.
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)