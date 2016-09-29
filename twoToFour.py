from math import exp


class Solver():
    def __init__(self):
        # self.test = testList()
        _ = 0

    def ai(self, test_list, learningRate):
        w1 = 0.5
        w2 = 0.5
        w3 = 0.5
        w4 = 0.5
        inp = [0] * 2
        net = [0] * 2
        out = [0] * 2
        facit = [0] * 2

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


if __name__ == "__main__":
    solver = Solver()

    # 3>2 --> True
    ins = list()
    outs = list()

    test = (ins, outs)

    test_list = list()
    test_list.append(test)

    solver.ai(test, 3)


def testList():
    test = list()
    # 0 to 3!
    for first in range(0, 4):
        for second in range(0, 4):
            if first >= second:
                test.append((first, second, True))
            else:
                test.append((first, second, False))
