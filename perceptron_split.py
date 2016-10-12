from image import Image
from outNode import OutNode
from inNode import InNode
from constants import Constants
import sys
import os
from random import shuffle

class PerceptronSplit():

    def __init__(self, image_train, facit_train, image_test, facit_test):
        self.constants = Constants(0.0006)
        folder = "./material/"
        self.imgTest  = Image(folder + image_test, folder + facit_test)
        self.imgTrain = Image(folder + image_train, folder + facit_train)
        self.create_neural_network(self.imgTrain)

    def reset_all(self):
        self.outs = []
        self.ins = []
        self.create_neural_network(self.imgTest)

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

    def train_set(self, imageHandler, imageTestHandler, nr_of_iterations):
        nr_of_images = len(imageHandler.get_images())
        nr_list = list(range(0,nr_of_images))

        for nr in range(0,nr_of_iterations):
            sum_error = 0
            shuffle(nr_list)

            for i in range(0,nr_of_images):
                img = imageHandler.get_image(nr_list[i])
                facit = imageHandler.get_facit(nr_list[i])
                self.train(img, facit)

                for out in self.outs_eyes:
                    sum_error += out.get_error(facit)

                for out in self.outs_mouth:
                    sum_error += out.get_error(facit)

            print("#Training {} / {}".format(nr + 1, nr_of_iterations))
            #print("sum error: {}\n".format(sum_error))

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

    def test_set(self, imageHandler):
        images = imageHandler.get_images()
        right = 0
        total = 0

        for i in range(0, len(images)):
            img = imageHandler.get_image(i)
            facit = imageHandler.get_facit(i)
            name = imageHandler.get_name(i)
            right += self.test(img, facit, name)
            total += 1

        percent = 100 * (float(right) / float(total))
        print("#percent right {}%".format(percent))

        return percent

    def test(self, image, facit, name):
        #resets previous result
        for out in self.outs:
            out.reset_value()

        #updates the input nodes
        self.update_inputs(image)

        #sends information via the edges to output
        for inp in self.nodes:
            inp.edges_to_out()

        #find maximum of outs (strongest guess)
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


        percent = list()

        for out in self.outs:
            percent.append(out.get_value() * 100)

        print("{} {} {}".format(name, answer, facit))
        correct = (answer == facit)
        if not correct:
            print("#Not correct ^")
        return correct


if __name__ == "__main__":
    image_path = sys.argv[1]
    facit_path = sys.argv[2]
    image_test_path = sys.argv[3]
    facit_test_path = sys.argv[4]

    folder = "./material/"

    if not os.path.exists(folder + image_path):
        print("could not find path"+folder + image_path)

    if not os.path.exists(folder + facit_path):
        print("could not find path"+folder + facit_path)

    if not os.path.exists(folder + image_test_path):
        print("could not find path"+folder + image_test_path)

    if not os.path.exists(folder + facit_test_path):
        print("could not find path"+folder + facit_test_path)

    print("#Loading and processing images")
    perceptron = PerceptronSplit(image_path, facit_path, image_test_path, facit_test_path)
    nr_of_iterations = 7

    perceptron.train_set(perceptron.imgTrain, perceptron.imgTest, nr_of_iterations)
    perceptron.test_set(perceptron.imgTest)







