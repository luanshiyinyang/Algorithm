# -*- coding:utf-8 -*-
'''
本模块实现一维数据的堆排序
'''


def HeapSort(data=[1, 2, 3, 4, 5]):
    def HeapAdjust(data, parent, length):
        '''
        调整为大顶堆
        :param data: 数据序列
        :param parent: 堆的父结点
        :param length: 数组长度
        :return:
        '''
        temp = data[parent]
        child = 2 * parent + 1
        while child <length:
            if child + 1 < length and data[child] < data[child+1]:
                child += 1
            if temp >= data[child]:
                break
            data[parent] = data[child]
            parent = child
            child = 2 * parent + 1
        data[parent] = temp

    length = len(data)
    for i in range(0, length//2)[::-1]:
        HeapAdjust(data, i, length)
    for j in range(1, length)[::-1]:
        data[j], data[0] = data[0], data[j]
        HeapAdjust(data, 0, j)
        print("第{}趟排序:".format(length-j), data)
    return None


if __name__ == '__main__':
    testData = [6, 4, 8, 9, 5, 2, 3, 1]
    HeapSort(testData)

