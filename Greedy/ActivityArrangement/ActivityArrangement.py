# -*-coding:utf-8-*-

def bubble_sort(s, f):
    """
    冒泡排序对结束时间排序，同时得到对应的开始时间的list
    :param s:
    :param f:
    :return:
    """
    for i in range(len(f)):
        for j in range(0, len(f)-i-1):
            if f[j] > f[j+1]:
                f[j], f[j+1] = f[j+1], f[j]
                s[j], s[j+1] = s[j+1], s[j]
    return s, f

def greedy(s, f, n):
    a = [True for x in range(n)]
    # 选择第一个活动
    j =0
    for i in range(1, n):
        # 如果下一个活动的开始时间大于等于上一个活动的结束时间
        if s[i] >= f[j]:
            a[i] = True
            j = i
        else:
            a[i] = False
        return a


if __name__ == '__main__':
    s = [1, 2, 3, 5, 8]
    f = [3, 4, 5, 7, 9]
    s, f = bubble_sort(s, f)
    A = greedy(s, f, len(s))
    res = []
    for k in range(len(A)):
        if A[k]:
            res.append('({}, {})'.format(s[k], f[k]))
    print(''.join(res))