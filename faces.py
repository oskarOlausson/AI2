import sys

from constants  import Constants
from image      import Image
from edge       import Edge

class Faces:
    def __init__(self, image_path, facit_path):
        self.main(image_path, facit_path)


    def main(self, image_path, facit_path):
        image = Image(image_path, facit_path)



#training
if __name__=="__main__":
    learning_rate = 0.1
    start_weight = 0.5
    constants = Constants(learning_rate, start_weight)

    image_path = sys.argv[1]
    facit_path = sys.argv[2]
    face = Faces(image_path, facit_path)

    image = face.get_current_image()

    #fore each image
    image_count = image.get_nr_of_images();
    for i in range(0, image_count):
        ins = list()
        edges = list()

        #loop an image and conect them to edges
        for i in range(0,201):
            for j in range(201):
                ins.apend( image.check_pixel(i,j) )
                edge = Edge(out, constants)
                edges.apend()

        # träna


    def train():
        edges =
        inp = [0] * 2
        net = [0] * 2
        out = [0] * 2
        facit = [0] * 2

        learningRate = constants.get_learning_rate()

        for ins, outs in test_list:
            number = 0

            inp[0] = test[number + 0]
            inp[1] = test[number + 1]

            net[0] = inp[0] * w1 + inp[1] * w2
            net[1] = inp[0] * w3 + inp[1] * w4

            out[0] = 1 / (1 + exp(-net[0]))
            out[1] = 1 / (1 + exp(-net[1]))

            facit[0] = test[number + 2]
            facit[1] = test[number + 3]

            w1_to_out1 = (out[0] - facit[0]) * out[0] * (1 - out[0]) * inp[0]
            w1 = w1 - (w1_to_out1 * learningRate)

            w2_to_out1 = (out[0] - facit[0]) * out[0] * (1 - out[0]) * inp[1]
            w2 = w2 - (w2_to_out1 * learningRate)

            w3_to_out2 = (out[1] - facit[1]) * out[1] * (1 - out[1]) * inp[0]
            w3 = w3 - (w3_to_out2 * learningRate)

            w4_to_out2 = (out[1] - facit[1]) * out[1] * (1 - out[1]) * inp[1]
            w4 = w4 - (w4_to_out2 * learningRate)

        print("w1: {}, w2: {}, w3: {}, w4: {}".format(w1, w2, w3, w4))
        print("out1: {}, out2: {}, in1: {}, in2: {}".format(out[0], out[1], inp[0], inp[1]))
