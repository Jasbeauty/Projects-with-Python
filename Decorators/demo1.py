#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/28 11:11 AM
# @Author: jasmine sun
# @File  : demo1.py

def makebold(fn):
    # 装饰器将返回新的函数
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello, world"


if __name__ == '__main__':
    print(hello())
