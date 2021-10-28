# /usr/bin/env python
# -*- coding: utf-8 -*-
# author__ = 'HanKai'
import pytest
# 只有调用open才执行
# @pytest.fixture()

# 每个测试函数都会自动调用该前置函数
# @pytest.fixture(autouse="true")

# 类下方法多个调用了，只执行一次
# @pytest.fixture(scope="class")

# 一个py文件是一个module，执行2和3 所以执行两次
# @pytest.fixture(scope="module")

# session级别只执行一次
@pytest.fixture(scope="session")
def open():
    print("打开浏览器")
    yield
    print(1+1)
    print("执行teardown !")
    print("最后关闭浏览器")
