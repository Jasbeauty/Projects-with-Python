#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/28 1:49 PM
# @Author: jasmine sun
# @File  : demo2.py


def decorator(fn):
    def wrapped(*args, **kwargs):
        print('do i have args ?')
        print(args)
        print(kwargs)
        fn(*args, **kwargs)

    return wrapped


@decorator
def fn1():
    print("python is cool")


@decorator
def fn2(a, b, c):
    print(a, b, c)


@decorator
def fn3(a, b, c='hello'):
    print(a, b, c)


if __name__ == '__main__':
    fn1()
    # fn2(1, 2, 3)
    fn3(1, 2, c='hi')
