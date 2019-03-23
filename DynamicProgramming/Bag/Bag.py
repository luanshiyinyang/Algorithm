def bag(i, j, w, v, out):
    if i == 0 and j >= 0:
        out[i][j] = 0
        return 0
    if i >= 0 and j == 0:
        out[i][j] = 0
        return 0
    if j - w[i-1] >= 0:
        out[i][j] = max(bag(i-1, j, w, v, out), v[i-1] + bag(i-1, j-w[i-1], w, v, out))
        return out[i][j]
    if j - w[i-1] < 0:
        out[i][j] = bag(i-1, j, w, v, out)
        return out[i][j]


def search(rst, i, j):
    x = [False for m in range(i+1)]
    for m in range(i, -1, -1):
        if rst[m][j] == rst[m-1][j]:
            # 此时代表没有选中当前
            pass
        else:
            x[m] = True
            j -= w[m-1]
    for i in range(len(x)):
        if x[i]:
            print("选择了第{}个物品".format(i))


if __name__ == '__main__':
    # 物品数目
    i = 5
    # 背包容量
    j = 10
    # 物品信息
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    # 结果存放表
    rst = [[0 for m in range(j+1)] for n in range(i+1)]
    # 计算结果，构造解集合
    bag(5, 10, w, v, out=rst)
    # 输出解集合表格
    for item in rst:
        print(item)
    # 回溯查找输入序列
    search(rst, i, j)
