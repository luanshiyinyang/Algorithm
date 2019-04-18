# -*-coding:utf-8-*-
def LSS(array):

    if array == []:
        return

    if len(array) == 1:
        return array[0]

    cut = len(array) // 2  # 设置中点
    left_sum = LSS(array[: cut])
    right_sum = LSS(array[cut:])

    # 从中点开始分别左右遍历查值

    left_middle_sum = 0
    max_l = 0
    right_middle_sum = 0
    max_r = 0
    for i in range(cut-1, -1, -1):
        left_middle_sum += array[i]
        max_l = max(left_middle_sum, max_l)
    for j in range(cut+1, len(array), 1):
        right_middle_sum += array[j]
        max_r = max(right_middle_sum, max_r)

    return max(left_sum, right_sum, max_l+max_r+array[cut])


if __name__ == '__main__':
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("input", array)
    rst = LSS(array)
    print(rst)