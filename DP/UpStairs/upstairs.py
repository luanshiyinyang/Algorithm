class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 3
        dp[0], dp[1], dp[2] = 1, 2, 0

        for i in range(2, n):
            dp[2] = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], dp[2]
            
        return dp[2] if n > 2 else dp[n-1]
