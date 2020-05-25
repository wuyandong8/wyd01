# -*- coding: utf-8 -*-
from test_01 import *


def test_add(x, y):
    data = add(1, 2)
    assert data == (x+y), "加法成立"
    print(data)


if __name__ == '__main__':
    test_add(1, 2)
    test_add(1, 3)