def getdp(arr):
    n = len(arr)
    dp, ends = [0] * n, [0] * n
    ends[0], dp[0] = arr[0], 1
    right, l, r, m = 0, 0, 0, 0
    for i in range(n):
        l = 0
        r = right
        # 二分查找，找不到则ends[l或r]是比arr[i]大而又最接近其的数
        # 若arr[i]比ends有效区的值都大，则l=right1
        while l <= r:
            m = int((l+r) / 2)
            if arr[i] > ends[m]:
                l = m + 1
            else:
                r = m - 1
        right = max(right, l)
        ends[l] = arr[i]
        dp[i] = l + 1
    return dp


def generate_lis(arr, dp):
    n = max(dp)
    index = dp.index(n)
    lis = [0] * n
    n -= 1
    lis[n] = arr[index]

    # 从右向左查
    for i in range(index, -1, -1):
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            n -= 1
            lis[n] = arr[i]
            index = i
    return lis


if __name__ == '__main__':
    arr = [3, 1, 4, 5, 9, 2, 6, 5, 0]
    print(generate_lis(arr, getdp(arr)))