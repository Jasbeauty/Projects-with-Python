#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/27 3:25 PM
# @Author: jasmine sun
# @File  : fibonacci.py
from functools import reduce


def fibo(num):
    #     list = []
    #     for i in range(num):
    #         if i == 0 or i == 1:
    #             list.append(1)
    #         else:
    #             list.append(list[i - 1] + list[i - 2])
    #     print('结果：', list[i])
    if num <= 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


def fibo1(n):
    fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)
    return fib(n)

    # print(type(fib))


if __name__ == '__main__':
    # num = input('输入Fibonacci位数: ')
    # fibo(int(num))
    n = input('输入n: ')
    result = fibo(int(n))
    print('结果为 {}'.format(result))
