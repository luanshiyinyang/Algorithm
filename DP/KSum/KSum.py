def dp(n, k, target, nums_list, rst):
    number_list = nums_list

    if k > n:
        return 0
    if n == 0 or k == 0:
        return 0
    if k == 1:
        for i in range(n):
            if number_list[i] == target:
                rst += 1
        return rst
    if n >= k:
        return dp(n-1, k-1, target-number_list[n-1], number_list, rst) + dp(n-1, k, target, number_list, rst)


if __name__ == '__main__':
    nums = [1, -1, 0, 1]
    n = len(nums)
    k = 3
    target = 0
    out = 0
    # 对这个题目而言就是填写dp[n][[k]的表格
    print(dp(len(nums), 3, 0, nums, out))