#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/11/26 10:06 AM
# @Author: jasmine sun
# @File  : list.py


def user_input():
    random_list = input("请以空格为间隔，输入一个整型数组：")
    format_list = list(map(int, random_list.split()))
    # print(format_list)
    return format_list


# 求解最长递增子序列及其长度
def longest_sub_increase_seq(array):
    # 求最长子序列，array为length个数的序列
    length = len(array)
    x = [1 for i in range(length)]
    z = [0 for i in range(length)]
    for i in range(1, length):
        index = i  # 记录使x[0..i]递增子序列最长的，倒数第二个位置
        maxnum = 1  # 递增序列的长度
        for j in range(i):
            if array[i] > array[j]:
                if maxnum < x[j] + 1:
                    index = j
                    maxnum = x[j] + 1
        z[i] = index
        x[i] = maxnum
    maxvalue = max(x)

    return_value = []
    for i in range(length):
        vv = []
        if x[i] == maxvalue:
            j = i
            while z[j] != j:
                vv.append(array[j])
                j = z[j]
            else:
                vv.append(array[j])
            return_value.append(vv)

    print('最长不连续递增子序列长度为: ' + str(len(return_value[0])))
    print('最长递增子序列: ' + str(return_value[0]))
    return return_value


def longest1(arrays):
    max = 0
    for i in range(len(arrays) - 1):
        count = 1
        min = arrays[i]
        for j in range(i + 1, len(arrays)):
            if min < arrays[j]:
                min = arrays[j]
                count += 1
            # 下面两句用于获取连续的递增子序列
            else:
                break
        if max < count:
            max = count
    return max


if __name__ == '__main__':
    arrays = [-1, 1, -1, 2, 1, 3, 1, 4, 5, 6, 7, 8]
    print(longest1(arrays))

    longest_sub_increase_seq(arrays)


