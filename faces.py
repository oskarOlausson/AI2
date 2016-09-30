import sys

from constants  import Constants
from image      import Image
from edge       import Edge
from outNode    import OutNode
from inNode     import InNode

class Faces:
    def __init__(self, image_path, facit_path):
        self.main(image_path, facit_path)


    def main(self, image_path, facit_path):
        self.image_handler = Image(image_path, facit_path)



if __name__=="__main__":
    learning_rate = 0.1
    start_weight = 0.5
    constants = Constants(learning_rate, start_weight)

    image_path = sys.argv[1]
    facit_path = sys.argv[2]
    face = Faces(image_path, facit_path)

    image = Image(image_path, facit_path)

    #fore each image
    image_count = len(image.get_images());
    for i in range(0, image_count):
        ins = list()

        #loop an image and conect them to edges
        for i in range(0,20):
            for j in range(20):

                edges = list()
                outs = list()
                for k in range(1,5):
                    out = OutNode(k)
                    outs.append(out)
                    edge = Edge(out, constants)
                    edges.append(edge)

                ins.append(InNode(image.check_pixel(i, j), outs, constants))

    def train(self):

        # for every image
        image_handler = self.image_handler
        images = image_handler.image.get_images()
        for i in range(0, len(images)):
            image = self.image_handler.get_image(i)

            #reset all out values
            for out in outs:
                out.reset_value()

            #update pixel
            for in_ in ins:
                for x in range(0,20):
                    for y in range(0,20):
                        in_.update_pixel(image.check_pixel(x,y))

                #update out
                in_.edges_to_out()

            #out preces
            for out in outs:
                out.process_out_value()

            for in_ in ins:
                in_.calculate_weights(image_handler.get_facit())