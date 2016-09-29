
class Image():

    def __init__(self,path,pathFacit):
        f = open(path)
        self.img = f.readlines()
        f.close()
        f = open(pathFacit)
        self.facit = self.parse_facit(f.readlines())
        self.image_number = 0
        f.close()

        self.current_line = 0
        self.current_image = self.parse_next_image()
        self.nr_of_images = self.readNrOfImages()

    def getFacit(self,index):
        return self.facit[index]

    def printFacit(self,index):
        value = self.facit[index]
        if value==1:
            return "happy"
        elif value==2:
            return "sad"
        elif value==3:
            return "trixy"
        elif value==4:
            return "mad"
        else:
            return "Unknown feeling"

    def readNrOfImages(self):
        information = self.img[1]
        for i in information.replace("(","( ").replace(" )"," ").split():
            if is_int(i):
                return int(i)
        return -1


    def reset_current_line(self):
        self.current_line = 0

    def find_next_image(self):
        stop = False
        while(not stop):
            line = self.img[self.current_line]
            stop = (line.find("Image")==0)
            if stop:
                a = line.split("e")
                b = a[1]
                c = int(b)
                self.image_number = c

            self.next_line()
            if stop: return self.current_line

    def parse_next_image(self):
        self.find_next_image()
        return self.parse_image()

    def parse_image_line(self):
        line = self.img[self.current_line].split()
        line = [int(x) for x in line if x != " "]
        return line

    def current_facit_index(self):
        return self.image_number - 1

    def next_line(self):
        self.current_line += 1
        return self.current_line

    def parse_image(self):
        image = list()
        for i in range(0,20):
            image.append(self.parse_image_line())
            self.next_line()
        return image

    def parse_facit(self,stringList):
        facitList = list()
        for row in stringList:
            if row.find("Image")==0:
                facitList.append(int(row.split()[1]))

        return facitList

    def check_pixel(self,x,y):
        return self.current_image[y][x]

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":

    img = Image('./material/training-A.txt','./material/facit-A.txt')

    print(img.image_number)
    print(img.printFacit(img.current_facit_index()))












