"""
该模块实现了一维数据集的冒泡排序
"""


def bubbleSort(data=[5, 4, 3, 2, 1]):
    for i in range(len(data)-1):
        print("第{}趟排序".format(i))
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print("当前排序结果为:", data)
    return None


def bubbleSortOptimized(data=[1, 2, 3, 4, 5]):
    for i in range(len(data)-1):
        flag = False
        print("第{}趟排序".format(i))
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                flag = True
        if flag is False:
            break
        print("当前排序结果为:", data)
    return None


if __name__ == '__main__':
    testData = [1, 3, 5, 7, 9, 8, 6, 4, 2]
    testData2 = [1, 2, 3, 4, 5, 6, 7, 9, 8]
    print("原来数据", testData)
    bubbleSort(testData)
    bubbleSortOptimized(testData2)
