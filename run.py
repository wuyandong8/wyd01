# -*- coding: utf-8 -*-
from test_01 import *


def test_add():
    data = add(1, 2)
    print(data)
    assert data == 3, "加法成立"


if __name__ == '__main__':
    test_add()