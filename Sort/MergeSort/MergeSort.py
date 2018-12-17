# -*- coding:UTF-8 -*-
def MergeSort(data=[1, 2, 3, 4, 5]):
    def merge(data, left, middle, right, temp):
        '''
        合并函数
        :param data: 待合并列表
        :param left:左指针
        :param middle:
        :param right:右指针
        :param temp:
        :return:None
        '''
        i = left
        j = middle + 1
        k = 0
        while i <= middle and j <= right:
            if data[i] <= data[j]:
                temp[k] = data[i]
                i += 1
            else:
                temp[k] = data[j]
                j += 1
            k += 1
        while i <= middle:
            temp[k] = data[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = data[j]
            j += 1
            k += 1
        k = 0
        while left <= right:
            data[left] = temp[k]
            left += 1
            k += 1

    def mergeSort(data, left, right, temp):
        print(data)
        if left < right:
            middle = (left + right) // 2
            mergeSort(data, left, middle, temp)
            mergeSort(data, middle+1, right, temp)
            merge(data, left, middle, right, temp)

    temp = [0]*len(data)
    mergeSort(data, 0, len(data)-1, temp)
    print(data)
    return data


if __name__ == '__main__':
    testData = [6, 5, 4, 3, 2, 7, 1]
    MergeSort(testData)