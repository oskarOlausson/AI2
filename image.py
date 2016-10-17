import numpy
from PIL import Image as Im
from math import atan2, pi

class Image():

    def __init__(self, path, path_facit):
        self.IMAGE_SIZE = 20

        f = open(path)
        self.img = f.readlines()
        f.close()

        if path_facit is not None:
            f = open(path_facit)
            self.facit = self.parse_facit(f.readlines())
            f.close()
        else:
            path_facit = None

        self.image_number = 0
        self.current_line = 0

        self.image_names = []
        #Parameter is wheather the images should be rotated
        self.images = self.create_image_list()

        self.current_image = self.images[0]

    def get_images(self):
        return self.images

    def create_image_list(self):
        """
        creates list of images
        :return: list of numpy array
        """
        self.current_line = 0
        images = list()

        img = self.parse_next_image()
        images.append(img)

        while img is not None:
            img = self.parse_next_image()
            if img is not None:
                img = self.rotate_image(img)
                images.append(img)

        return images

    def get_facit(self, index):
        if self.facit is not None:
            return self.facit[index]
        else:
            return None

    def get_name(self, index):
        return self.image_names[index]

    def get_image(self, index):
        return self.images[index]

    def get_current_image(self):
        return self.current_image

    def find_next_image(self):
        """
        reads until next image is found
        (also reads in image names)
        :return: line index
        """
        stop = False
        while (not stop):
            line = self.img[self.current_line]
            found_index = line.find("Image")
            stop = (found_index == 0)
            if stop:
                self.image_names.append(line.rstrip())
                a = line.split("e")
                b = a[1]
                c = int(b)
                self.image_number = c

            self.next_line()
            if self.current_line > len(self.img) - 1: return -1

        return self.current_line

    def rotate_image(self, img):
        """
        rotates the image so the eyes are at the top
        """
        cx, cy = 9, 9
        index = 0

        index += 1
        mx, my = self.find_eyes(img)
        angle = atan2(mx - cx, my - cy)

        angle *= 180 / pi

        a = angle - -90
        a = ((a + 180) % (360)) - 180

        graphic = Im.fromarray(img)
        graphic = graphic.rotate(a)

        array = numpy.asarray(graphic, dtype = numpy.uint8)

        return array

    def parse_next_image(self):
        """
        reads until next image an returns it
        :return: numpy array
        """
        if self.find_next_image() != -1:
            return self.parse_image_numpy()
        else:
            return None

    def parse_image_line(self):
        line = self.img[self.current_line].split()
        line = [int(x) for x in line if x != " "]
        return line

    def next_line(self):
        self.current_line += 1
        return self.current_line

    def parse_image_numpy(self):
        image = numpy.zeros((self.IMAGE_SIZE, self.IMAGE_SIZE))
        for y in range(0, self.IMAGE_SIZE):
            str = self.parse_image_line()
            for x in range(0,len(str)):
                image[x][y] = str[x]
            self.next_line()
        return image

    def parse_facit(self, stringList):
        """
        checks what the facit is
        :return:
        """
        facitList = list()
        for row in stringList:
            if row.find("Image") == 0:
                facitList.append(int(row.split()[1]))

        return facitList

    def find_eyes(self, image):
        """
        finds the eyes by checking the average position of the 26 darkest pixels
        :return: that average position
        """
        length = 26
        dark_spots = [0] * length
        dark_positions = [(0, 0)] * length

        for y in range(0, self.IMAGE_SIZE):
            for x in range(0, self.IMAGE_SIZE):
                value = image[x][y]
                index = len(dark_spots) - 1
                while value >= dark_spots[index] and index > 0:
                    index -= 1

                if index < len(dark_spots) - 1:
                    dark_spots.insert(index, value)
                    dark_positions.insert(index, (x, y))
                    # remove the last so the list does not get longer
                    dark_spots.pop(len(dark_spots) - 1)
                    dark_positions.pop(len(dark_positions) - 1)

        mx, my = (0, 0)
        for index in dark_positions:
            ax, ay = index
            mx += ax
            my += ay

        mx /= len(dark_positions)
        my /= len(dark_positions)

        return mx, my













