#-*- coding:UTF-8 -*-
"""
本模块演示了一维数据的简单选择排序
"""


def SelectSort(data=[1, 2, 3, 4, 5]):
    length = len(data)
    for i in range(length):
        min = i
        for j in range(i+1, length):
            if data[min] > data[j]:
                min = j
        data[min], data[i] = data[i], data[min]
        print("第{}趟排序结果".format(i), data)


if __name__ == '__main__':
    testData = [1, 3, 2]
    SelectSort(testData)



