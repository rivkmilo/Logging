import sys
from modules import math_ops

if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    math_ops._add(x, y)
    math_ops._sub(x, y)
    math_ops._mul(x, y)
    math_ops._div(x, y)