import numpy
from PIL import Image as Im
from math import atan2, pi

class Image():

    def __init__(self, path, pathFacit):

        f = open(path)
        self.img = f.readlines()
        f.close()

        f = open(pathFacit)
        self.facit = self.parse_facit(f.readlines())
        f.close()

        self.image_number = 0
        self.current_line = 0

        self.image_names = []
        #Parameter is wheather the images should be rotated
        self.images = self.create_image_list(True)

        self.current_image = self.images[0]
        self.nr_of_images = self.read_nr_of_images()

    def get_images(self):
        return self.images

    def create_image_list(self, rotate):
        self.current_line = 0
        images = list()

        img = self.parse_next_image()
        images.append(img)

        while img is not None:
            img = self.parse_next_image()
            if img is not None:
                if rotate: img = self.rotate_image(img)
                images.append(img)

        return images

    def get_facit(self, index):
        return self.facit[index]

    def get_name(self, index):
        return self.image_names[index]

    def get_image(self, index):
        return self.images[index]

    def get_current_image(self):
        return self.current_image

    def read_nr_of_images(self):
        information = self.img[1]
        for i in information.replace("(", "( ").replace(" )", " ").split():
            if is_int(i):
                return int(i)
        return -1

    def reset_current_line(self):
        self.current_line = 0

    def find_next_image(self):
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

        cx, cy = 9, 9
        index = 0

        index += 1
        mx, my = find_eyes(img)
        angle = atan2(mx - cx, my - cy)

        angle *= 180 / pi

        a = angle - -90
        a = ((a + 180) % (360)) - 180

        graphic = Im.fromarray(img)
        graphic = graphic.rotate(a)

        array = numpy.asarray(graphic, dtype = numpy.uint8)

        return array

    def save_all(self):

        for index in range(0,len(self.images)):

            img = self.images[index]
            img = img.T
            for y in range(0,20):
                for x in range(0,20):
                    img[x][y] = 255 - (img[x][y] * float(255) / 32)

            graphic = Im.fromarray(img)
            graphic = graphic.convert('RGB')
            graphic.save('./pictures/face_img_' + self.image_names[index] + '.jpg')

    def parse_next_image(self):
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
        image = numpy.zeros((20, 20))
        for y in range(0, 20):
            str = self.parse_image_line()
            for x in range(0,len(str)):
                image[x][y] = str[x]
            self.next_line()
        return image

    def parse_facit(self, stringList):
        facitList = list()
        for row in stringList:
            if row.find("Image") == 0:
                facitList.append(int(row.split()[1]))

        return facitList


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def find_eyes(image):

    length = 26
    dark_spots = [0] * length
    dark_positions = [(0,0)] * length

    for y in range(0, 20):
        for x in range(0, 20):
            value = image[x][y]
            index = len(dark_spots) - 1
            while value >= dark_spots[index] and index > 0:
                index -= 1

            if index < len(dark_spots) - 1:
                dark_spots.insert(index,value)
                dark_positions.insert(index,(x,y))
                #remove the last so the list does not get longer
                dark_spots.pop(len(dark_spots)-1)
                dark_positions.pop(len(dark_positions)-1)


    mx, my = (0, 0)
    for index in dark_positions:
        ax, ay = index
        mx += ax
        my += ay

    mx /= len(dark_positions)
    my /= len(dark_positions)

    return mx, my

if __name__ == "__main__":

    img = Image('./material/training-A.txt', './material/facit-A.txt')
    img.rotate_image(img.get_image(0))












