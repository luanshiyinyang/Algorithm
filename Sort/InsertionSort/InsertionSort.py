"""
本模块实现一位数据的直接插入排序及其优化
"""


def insertSort(data=[0, 1, 2, 3, 4, 5]):
    for i in range(1, len(data)):
        # 从下标1开始记录每一个待排元素
        temp = data[i]
        # 从当前元素的前一个元素开始进行合适位置查找
        j = i - 1
        while j >= 0 and temp < data[j]:
            # 循环直到序列第一个值或者找到一个元素比它小,循环内不断将元素向后交换
            data[j+1] = data[j]
            j -= 1
        data[j+1] = temp
    print(data)


def binarySearch(inputData, endIndex, value):
    '''

    :param inputData: 数据集
    :param endIndex: 查找结束位置
    :param value: 查找的值
    :return:
    '''
    left = 0
    right = endIndex - 1
    while left <= right:
        middle = left + (right-left) // 2
        if inputData[middle] >= value:
            right = middle - 1
        else:
            left = middle + 1
    return left if left < endIndex else -1


def insertSortOptimized(data=[0, 1, 2, 3, 4, 5]):
    for i in range(1, len(data)):
        j = i - 1
        temp = data[i]
        insertIndex = binarySearch(data, i, data[i])
        if insertIndex != -1:
            while j >= insertIndex:
                data[j+1] = data[j]
                j -= 1
        data[j+1] = temp
    print(data)


if __name__ == '__main__':
    testData1 = [1, 2, 3, 5, 4, 0]
    insertSort(data=testData1)
    insertSortOptimized(testData1)