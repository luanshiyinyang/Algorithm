def dp(n, k, target, nums_list, dp_list):
    number_list = nums_list

    if k > n:
        dp_list[n][k][target] = 0
        return 0
    if n == 0 or k == 0:
        dp_list[n][k][target] = 0
        return 0
    if k == 1:
        for i in range(n):
            if number_list[i] == target:
                out += 1
        return out
    if n >= k:
        return dp(n-1, k-1, target-number_list[n-1], number_list,) + dp(n-1, k, target, number_list,)


if __name__ == '__main__':
    nums = [1, -1, 0]
    n = len(nums)
    k = 3
    target = 0
    out = 0
    # 对这个题目而言就是填写dp[n][[k]的表格
    import copy
    init_list = [0] * 10
    print(dp(len(nums), 3, 0, nums, dp_list))