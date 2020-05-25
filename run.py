# -*- coding: utf-8 -*-
from test_01 import *


def test_add():
    data = add(1, 2)
    assert data == 4, "加法成立"
    print(data)


if __name__ == '__main__':
    test_add()