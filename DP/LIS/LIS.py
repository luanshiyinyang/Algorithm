def f(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
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
    print(generate_lis(arr, f(arr)))