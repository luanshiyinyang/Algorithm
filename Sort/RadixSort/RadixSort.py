# -*- coding:UTF-8 -*-
"""
本模块实现了一维整形数的基数排序
"""
def RadixSort(data=[1, 2, 3, 4, 5]):
    def getMaxBit(data):
        '''
        求出最大数的位数
        :param data:
        :return:
        '''
        maxData = max(data)
        bitsNum = 0
        while maxData:
            bitsNum += 1
            maxData //= 10
        return bitsNum


    def getDigit(number, n):
        '''
        取number第n位数字
        :param number:
        :param n:
        :return:
        '''
        p = 1
        while n > 1:
            n -= 1
            p *= 10
        return number // p % 10

    length = len(data)
    bucket = [0]*length
    for d in range(1, getMaxBit(data)+1):
        count = [0]*10
        for i in range(length):
            count[getDigit(data[i], d)] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(0, length)[::-1]:
            k = getDigit(data[i], d)
            bucket[count[k] - 1] = data[i]
            count[k] -= 1
        for i in range(0, length):
            data[i] = bucket[i]
    print(data)
    return None


if __name__ == '__main__':
    testData = [50, 123, 456, 187, 4, 11, 100]
    RadixSort(testData)