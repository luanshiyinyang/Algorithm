# 爬楼梯问题
## 动态规划
动态规划算法将带求解问题拆分成一系列相互交叠的子问题，通过递推关系定义各子问题的求解策略，并随时记录子问题的解，最终获得原始问题的解，避免了对交叠子问题的重复求解。

在动态规划算法中有三要素，即**最优子结构、边界和状态转移函数**。
- 最优子结构是指每个阶段的最优状态可以由之前某个阶段的某个或某些状态直接得到。
- 边界是指问题最小子集的解；（代码中就是递归的出口或者dp数组的初始值）
- 状态转移函数是指从一个阶段向另一个阶段过渡的具体模式，描述的是两个相邻子问题之间的关系。

凡是具有这三个要素的问题均可以使用动态规划求解。

## 爬楼梯
 本案例是一个简单基础的问题---爬楼梯问题，原题来自Leetcode题库[第70题](https://leetcode-cn.com/problems/climbing-stairs/)，难度为Easy。

### 问题描述
假设小明要怕一个10级的楼梯，一步走一级或者一步走两级，问他走到顶有多少种方法。举个例子，他可以每次走一步，那么他走了10步；他也可以一次走两步，他走了5步；解题的人要找到所有走的方案数。

**示例1：**
```
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
```
**示例2：**
```
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
```

### 问题分析
我们不妨直接看最后一步，他要么是从第九级再走一级到顶，要么是从第八级走两步到顶。也就是说，最后那一步要么从第九级出发（这时只有唯一路径，就是走一级）；要么从第八级出发（这时只有唯一路径，走两级；如果走两个一级，那么这种情况就是第一种的内容了）。换句话说，一旦知道从地面到第八级有X种走法，从地面到第九级有Y种走法，那么从地面到顶就是X+Y种走法。

为了方便描述，用$F(n)$表示第n级台阶的走法数量，可知$F(10)=F(9)+f(8)$。推广一下，就是下式。

$$F(n)=F(n-1)+F(n-2)$$

**这就是我们想要的状态转移函数和最优子结构。**  当问题细化，只有一级台阶和两级台阶时，不再细化，$F(1)=1,F(2)=2$，**这其实就是边界。**

该问题动态规划解法的三要素全都出现了，分别如下：
- 边界：$F(1)=1,F(2)=2$
- 最优子结构：$F(n-1)和F(n-2)$
- 状态转移函数：$F(n)=F(n-1)+F(n-2)$

也就是说，这个问题的动态规划建模完成了，为了时间和空间的效率（特别对于大问题），利用最优子结构的特性，**我们一般采用自底向上的方式计算，也就是维护dp数组**。也就是根据1、2算3，根据2、3算4，以此类推。

这个解法的基础递归代码如下，这是自顶而下的解法。

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n):
            if n < 1:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n > 2:
                return dp(n-1) + dp(n-2)
        return dp(n)
```

### 优化思路
上述这种基础的递归解法其实是存在**大量的重叠子问题**的，这是因为递归是对每个问题直接追溯到底层求解的，这中间存在大量的重复求解。举个例子，当我们计算$F(10)$的时候需要去计算$F(8)$和$F(9)$，但是，实际上我们在计算$F(9)$的时候也计算了$F(8)$，这就是为什么上述递归解法平台提交会出现**TLE超时错误**的原因。

优化的思路就是通过DP Table来存储之前已求得的解，以自底而上的思路求解,，因此代码可以优化如下。

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1) if n >= 3 else [0] * 3
        dp[0], dp[1], dp[2] = 0, 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
```

### 进一步优化
上述的解法是可以在平台上AC的，但是我们其实可以进一步优化，我们可以发现，其实为了求得最终解，我们始终使用的只有数组中的三个元素而已，因此不需要维护长度为n的数组空间，而是三个变量空间即可。**这个思路叫做状态压缩，它可以大大节省空间开销。**

代码如下。

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 3
        dp[0], dp[1], dp[2] = 1, 2, 0

        for i in range(2, n):
            dp[2] = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], dp[2]
            
        return dp[2] if n > 2 else dp[n-1]
```

## 补充说明
本文参考书为《你也能看得懂的Python算法书》，具体代码可以查看[我的Github](https://github.com/luanshiyinyang/Algorithm/tree/master/DP/UpStairs)，欢迎Star或者Fork。