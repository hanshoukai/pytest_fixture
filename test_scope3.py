# /usr/bin/env python
# -*- coding: utf-8 -*-
# author__ = 'HanKai'
import pytest

class TestFunc:
    def test_case1(self, open):
        print("test_case1，需要登录")
        # self.aa = open

    def test_case2(self, open):
        print("test_case2，不需要登录 ")

    def test_case3(self, open):
        print("test_case3，需要登录")


# if __name__ == '__main__':
#     pytest.main()