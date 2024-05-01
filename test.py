# Test unit for ML libarary

from vector import Vector
from vector import stack


def test():
    a = Vector([0, 1, 2])
    b = Vector([3, 4, 5])

    print(stack(a, b))


if __name__ == "__main__":
    test()
