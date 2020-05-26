# -*- coding: utf-8 -*-
from test_01 import *
import pytest
import os


if __name__ == '__main__':
    pytest.main(['-s', "-q", 'run.py', '--alluredir', './report/xml'])
    os.system("allure generate --clean ./report/xml -o ./report/html")