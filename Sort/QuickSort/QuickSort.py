# -*- coding:UTF-8 -*-
"""
本模块完成一维序列的快速排序
"""


def QuickSort(data=[1, 2, 3, 4, 5], left=0, right=1):
    def divide(inputList, left, right):
        '''
        根据left和right进行一次扫描，找到新的base
        :param inputList:
        :param left:
        :param right:
        :return:新base位置
        '''
        base = inputList[left]
        while left < right:
            while left < right and inputList[right] >= base:
                right -= 1
            inputList[left] = inputList[right]
            while left < right and inputList[left] <= base:
                left += 1
            inputList[right] = inputList[left]
        inputList[left] = base
        return left
    if left < right:
        baseIndex = divide(data, left, right)
        QuickSort(data, left, baseIndex-1)
        QuickSort(data, baseIndex+1, right)


if __name__ == '__main__':
    testData = [2, 4, 5, 1, 3]
    print("Raw Data:", testData)
    QuickSort(testData, 0, len(testData)-1)
    print("After Sort:", testData)

