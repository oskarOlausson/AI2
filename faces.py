
from perceptron_split import PerceptronSplit as Perceptron
import sys
import os

if __name__ == "__main__":
    image_path = sys.argv[1]
    facit_path = sys.argv[2]
    image_test_path = sys.argv[3]

    folder = "./material/"

    if not os.path.exists(folder + image_path):
        if not os.path.exists(image_path):
            print("#could not find path" + folder + image_path)
            exit(1)
    else:
        image_path = folder + image_path

    if not os.path.exists(folder + facit_path):
        if not os.path.exists(image_path):
            print("#could not find path" + folder + facit_path)
            exit(1)
    else:
        facit_path = folder + facit_path

    if not os.path.exists(folder + image_test_path):
        if not os.path.exists(image_path):
            print("#could not find path" + folder + image_test_path)
            exit(1)
    else:
        image_test_path = folder + image_test_path

    print("#Loading and processing images", file = sys.stderr)
    perceptron = Perceptron(image_path, facit_path, image_test_path)
    threash_hold = 0.01
    perceptron.train_set(perceptron.imgTrain, threash_hold)
    perceptron.real_test_set(perceptron.imgTest)