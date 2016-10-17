from image import Image
from outNode import OutNode
from inNode import InNode
from constants import Constants
import sys
from random import shuffle

class PerceptronSplit():


    def __init__(self, image_train, facit_train, image_test):
        self.constants = Constants(0.0006)

        self.imgTrain = Image(image_train, facit_train)
        self.imgTest = Image(image_test, None)
        self.create_neural_network(self.imgTrain)

    def create_neural_network(self, image):
        self.outs_eyes = list()
        self.outs_mouth = list()

        for i in range(2):
            self.outs_eyes.append(OutNode(i + 1, True))

        for i in range(2):
            self.outs_mouth.append(OutNode(i + 1, False))

        self.outs = self.outs_eyes + self.outs_mouth

        self.nodes = list()

        for y in range(0, 20):
            for x in range(0, 20):
                if y < 10:
                    self.nodes.append(InNode(None, self.outs_eyes, self.constants))
                else: self.nodes.append(InNode(None, self.outs_mouth, self.constants))

        self.update_inputs(image.get_image(0))
        #bias
        self.nodes.append(InNode(1, self.outs_eyes, self.constants))
        self.nodes.append(InNode(1, self.outs_mouth, self.constants))

    def train_set(self, image_handler, threash_hold):
        nr_of_images = len(image_handler.get_images())
        nr_list = list(range(0,nr_of_images))

        #making sure the loop starts
        sum_error = threash_hold + 1
        nr_of_iterations = 0

        while(sum_error > threash_hold and nr_of_iterations < 10):
            sum_error = 0
            shuffle(nr_list)

            for i in range(0,nr_of_images):
                img = image_handler.get_image(nr_list[i])
                facit = image_handler.get_facit(nr_list[i])
                self.train(img, facit)

                for out in self.outs:
                    sum_error += (out.get_error(facit) ** 2)

            sum_error /= nr_of_images
            nr_of_iterations += 1
            print("#Training error is {:.3}, threash hold is {}".format(sum_error, threash_hold), file = sys.stderr)

    def train(self, image, facit):
        #resets the out-nodes so the previous guess does not affect the current guess
        for out in self.outs:
            out.reset_value()

        #sends the pixel-values to the input-nodes
        self.update_inputs(image)

        #sends the information via the edges to the outputs
        for inp in self.nodes:
            inp.edges_to_out()

        #output processing the 1 / (1 + e^(-net))
        for out in self.outs:
            out.process_out_value()

        #reweights the edges
        for inp in self.nodes:
            inp.calculate_weights(facit)

    def update_inputs(self, image):
        index = 0
        for y in range(0, 20):
            for x in range(0, 20):
                pixel = image[y][x]

                self.nodes[index].update_pixel(pixel)
                index += 1

    def real_test_set(self, image_handler):
        length = len(image_handler.get_images())

        for i in range(0, length):
            img = image_handler.get_image(i)
            name = image_handler.get_name(i)
            self.real_test(img, name)

    def real_test(self, image, name):
        # resets previous result
        for out in self.outs:
            out.reset_value()

        # updates the input nodes
        self.update_inputs(image)

        # sends information via the edges to output
        for inp in self.nodes:
            inp.edges_to_out()

        # find maximum of outs (strongest guess)
        max = 0
        index = 0
        eye = None

        for out in self.outs_eyes:
            value = out.process_out_value()
            if value > max:
                max = value
                eye = out
            index += 1

        max = 0
        index = 0
        mouth = None

        for out in self.outs_mouth:
            value = out.process_out_value()
            if value > max:
                max = value
                mouth = out
            index += 1

        if eye.get_goal_value() == 1:
            if mouth.get_goal_value() == 1:
                answer = 1
            else:
                answer = 2
        else:
            if mouth.get_goal_value() == 1:
                answer = 3
            else:
                answer = 4
        string = "{} {}\n".format(name, answer)
        print(string, end="")





