import sys


class Faces:
    def __init__(self, image_path, facit_path):
        self.main(image_path, facit_path)

    def main(self, image_path, facit_path):
        image = Image(image_path, facit_path)


if __name__ == "__main__":
    image_path = sys.argv[1]
    facit_path = sys.argv[2]
    face = Faces(image_path, facit_path)
