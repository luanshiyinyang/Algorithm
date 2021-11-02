def bubble_sort(data):
    for i in range(len(data)-1):
        print("第{}趟排序".format(i))
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print("当前排序结果为:", data)
    return None

test_data = [1, 3, 5, 7, 9, 8, 6, 4, 2]
print("原来数据", test_data)
bubble_sort(test_data)


def bubble_sort_optimized(data):
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
test_data = [1, 2, 3, 4, 5, 6, 7, 9, 8]
print("原来数据", test_data)
bubble_sort_optimized(test_data)
