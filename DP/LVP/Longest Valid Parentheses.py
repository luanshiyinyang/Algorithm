class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0

        dp = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == "(":
                pass
            else:
                if i-1 >= 0:
                    if s[i - 1] == "(":
                        # 此时和i号字符匹配的已经找到
                        dp[i] = dp[i - 2] + 2
                    else:
                        # 此时这个右括号可能是一个合法子串的结尾也可能不是
                        if s[i-1- dp[i - 1]] == "(" and i-1-dp[i-1] >=0:
                            dp[i] = 2 + dp[i - 1] + dp[i-1-dp[i-1]-1]
                        else:
                            pass
        return max(dp)