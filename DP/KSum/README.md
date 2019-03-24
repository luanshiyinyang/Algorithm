# KSum问题
- 简述
	- CCF、LeetCode这类程序设计竞赛的常见题型。
-  问题描述
	-  给定一个n个数字的序列（均为整数），求k个数字的和为target的情况有多少种？
	-  注意，这里是依据下标选数，也就是说两种情况三个数字一样但是有一个数字的下标在两个情况中不一样，那么算作两种情况。
	-  这种题目只要一个最后结果可以使用递归迅速解答，本质上是在填一个二维表；如果要输出所有情况，本质上是填一个三维表。
- 问题分析
	- F(n,k,target)表示n个数里面选k个数和为target的情况数目。
	- n个数字里面k个数的和是否为target，可以分为两种情况：第n个数字被选了=F(n-1,k-1,target-nums[n])；第n个数字没有选=F(n-1,k,target)。结果是这两种情况的和。可以依次类推下去。
	- 得到边界和状态转移函数为
		- F(n,k,target)=0;n<k
		- F(n,k,target)=0;n=0 or k = 0
		- F(n,k,target)=m; k=1(m为从0到n的元素中值为target的元素个数）
		- F(n,k,target)=F(n-1,k-1,target-nums[n])+F(n-1,k,target);n>=k
	- 由此，不难写出递归思路的代码。
- 代码
	- ```python
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
		```
- 补充说明
	- 这种递归做法虽然可以迅速解答，但是不利于填表去回溯查找每种情况的具体取值，后面会使用循环填表来完成这一题。
	- 具体代码和更多算法类问题见我的Github，欢迎Star或者fork。