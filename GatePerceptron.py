class Perceptron:
    def __init__(self, bias=0.0):
        self.bias = bias
        self.w1 = 0
        self.w2 = 0

    def FProp(self, x1, x2):
        tmp = (x1 * self.w1) + (x2 * self.w2) + self.bias
        if tmp <= 0:
            return 0
        else:
            return 1

    def set_weight(self, w1, w2):
        self.w1 = w1
        self.w2 = w2


if __name__ == "__main__":
    # truth_data = [(0.8, 0.8)]
    # truth_data = [(0.5, 0.5)]
    truth_data = [(0, 0), (0, 1), (1, 0), (1, 1)]

    # AND 게이트
    AND = Perceptron(-0.7)
    AND.set_weight(0.5, 0.5)

    for i in truth_data:
        print("AND", i, "->", AND.FProp(*i))
    print()

    # NAND 게이트
    NAND = Perceptron(0.7)
    NAND.set_weight(-0.5, -0.5)

    for i in truth_data:
        print("NAND", i, "->", NAND.FProp(*i))
    print()

    # OR 게이트
    OR = Perceptron(-0.2)
    OR.set_weight(0.5, 0.5)

    for i in truth_data:
        print("OR", i, "->", OR.FProp(*i))
    print()

    # XOR 게이트 (다중 퍼셉트론)
    for i in truth_data:
        print("XOR", i, "->", AND.FProp(NAND.FProp(*i), OR.FProp(*i)))
    print()
