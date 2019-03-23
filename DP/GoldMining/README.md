# 矿工挖矿问题
- 简述
	- 为了解决在给定金矿和矿工数量的前提下，能够获得最多黄金的挖矿策略。
	- 很多算法题其实就是这个问题换了一个情境。
- 问题描述
	- 有5个金矿，每个金矿黄金储量不同，需要参与挖掘的工人数目也不同，假定有10个工人，每个金矿要么全挖，要么不挖，不可以拆分，试问，想得到最多的黄金，应该选择挖取哪几个金矿。
	- 金矿信息如下表。

		| 金矿编号| 黄金储量 | 所需工人数目 |
		| :---: | :---: | :---: |
		| 1 | 400 | 5 |
		| 2 | 500 | 5 |
		| 3 | 200 | 3 |
		| 4 | 300 | 4 |
		| 5 | 350 | 3 |
- 问题分析
	- 如果要使用动态规划解题，就要确定动态规划的三要素：最优子结构、边界和状态转移函数。
	- 最优子结构
		- 解题目标是确定10个工人挖5个金矿能够获得最多的黄金量，该问题可以从10个工人挖4个金矿的子问题中递归求解。
		- 在解决10个工人挖4个金矿时，存在两种选择，一种是放弃第5个矿，将10个工人投入到挖四个矿中；另一种选择是决定对第5个矿进行挖掘，因此需要从这10个人中抽取3个人（第5个矿需要人数）加入第5个矿开采，剩余的人处理前4个矿。
		- 因此，最优解应该是这两种选择中获得黄金数量较多的那一种。
		- 为了描述方便，设金矿数量为n，工人个数为w，第n个矿的黄金数量为G(n),第n个矿所需工人为P(n)，要想获得10个矿工挖掘5个金矿的最优解为max(F(4,10),F(4,10-P[4])+G[4])。
		- 这就是**最优子结构**。
	- 边界
		- 对于一个金矿而言，若当前的矿工数量不能达到金矿的挖掘需要，则获得的黄金数量为0，若能满足矿工数量要求，获得的黄金数量为G[0]。
		- 因此，边界可以描述为
			- n=1,w>=P[0]时，F(n,w)=G[0]
			- n=1,w<P[0]时，F(n,w)=0
	- 状态转移函数
		- F(n,w) = 0 (n<=1,w<p[0])
		- F(n,w) = G[0](n==1, w>=P[0])
		- F(n,w) = F(n-1,w)(n>1,w<P[n-1])
		- F(n,w) = max(F(n-1,w), F(n-1, w-P[n-1])+G[n-1])(n>1,w>=P[n-1])
	- 到这里，三要素找到了，经过这个过程也明白了求解过程，由底向上计算，一步步推导可以得到结果，换句话说，n步的解其实就是第一步的结果推来的，这就是递归过程。
- 代码
	- ```python
		def gold_mining(n ,w, G, P):
		    """
		    利用递归实现动态规划算法过程
		    :param n:
		    :param w:
		    :param G:
		    :param P:
		    :return:
		    """
		    if n <= 1 and w < P[0]:
		        return 0
		    if n == 1 and w >= P[0]:
		        return G[0]
		    if n > 1 and w < P[n-1]:
		        return gold_mining(n-1, w, G, P)
		    if n > 1 and w >= P[n-1]:
		        return max(gold_mining(n-1, w, G, P), gold_mining(n-1, w-P[n-1], G, P) + G[n-1])
		
		
		if __name__ == '__main__':
		    G = [400, 500, 200, 300, 350]
		    P = [5, 5, 3, 4, 3]
		    n = 5
		    w = 10
		    print(gold_mining(n, w, G, P))
		```
- 补充说明
	- 具体代码可以查看我的Github，欢迎Star或者Fork
	- 参考书《你也能看得懂的Python算法书》，书中略微有一点不合理之处，做了修改
	- 到这里，其实你已经体会到了动态规划的简约之美，当然，要注意Python是有递归深度限制的，如不是必要，建议使用循环控制