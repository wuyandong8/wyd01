# -*- coding: utf-8 -*-
from test_01 import *
import pytest
import os

@pytest.fixture()
def login():
    print('输入账号和密码')


def test_01(login):
    print('test1----')


def test_02():
    print('test2----不登录')


def test_03(login):
    print('test3----')



