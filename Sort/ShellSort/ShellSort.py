# -*- coding:UTF-8 -*-
"""
本模块完成数据序列的希尔排序
"""


def ShellSort(data=[1, 2, 3, 4, 5]):
    length = len(data)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            j = i - gap
            temp = data[i]
            # 对每一列进行排序,就是直接插入的思路
            while j >= 0 and temp < data[j]:
                data[j+gap] = data[j]
                j -= gap
                data[j+gap] = temp
        print("以步长为{}进行，结果为:".format(gap), data)
        gap //= 2
    return None


if __name__ == '__main__':
    testData = [10, 14, 73, 25,
                23, 13, 27, 94,
                33, 39, 25, 59,
                94, 65, 82, 45]
    ShellSort(testData)