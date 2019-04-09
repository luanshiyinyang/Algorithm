# 寻找制高点
- 简介
	- 比较基础的BFS问题，但是是很多算法题的模板。
- 问题描述
	- 现在，有一个矩阵，矩阵的每个值代表山的高度（均大于1），现在要求找到这个山的所有制高点。
	- 制高点指的是通过这个点可以从上下左右四个边界走出去这个矩阵平面，注意，是四个边界都能走出去。
	- 在整个平面的移动规则是从一个点只可以向上下左右四个方向走，并且只能走到不大于自己的值的位置上去。
- 问题分析
	- 这是一个典型的搜索问题，一开始的思路一定是从每个位置出发搜索其能否到达四个边缘。很显然，对矩阵的每个值都要进行这样的搜索，显然，这样有些费时了。（如果在LeetCode上，这就是Exceed Time Limit报错）
	- 那么，如何优化算法呢？
		- 这条思路不行，那么就换一个思路处理问题，既然从每个点走向边缘的搜索有些低效，那么不妨以边缘的所有点为起点向内部进行搜索，看下一个节点是否不小于自己的值（这和下山的规则相反）。
		- 标记能够到达的点为True，继续搜索，直到不能走为止。按照这样的思路，标记四个边界可以到达的点，都为True的点为制高点。（也就是四个集合的交集）
		- 这就是典型的逆向思维，算法中经常要求这种逆向思维。
	- 为了获取每个点，定义每个点的坐标为四个集合的记录值。
- 代码
	- ```python
		# -*-coding:utf-8-*-
		
		
		def bfs(set_data, m, n, matrx):
		    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
		    queue = list(set_data)
		    while queue:
		        x, y = queue.pop()
		        for d in dir:
		            nx, ny = x + d[0], y + d[1]
		            if 0 <= nx < m and 0 <= ny < n:
		                if matrix[nx][ny] >= matrix[x][y]:  # 如果新点不低于自己则可以走
		                    if (nx, ny) not in set_data:
		                        queue.append((nx, ny))
		                        set_data.add((nx, ny))
		
		
		def solve(matrix):
		    """
		    典型的BFS
		    :return:
		    """
		    m = len(matrix)
		    n = len(matrix[0])
		    top_point = set([(0, y) for y in range(n)])
		    bottom_point = set([(m-1, y) for y in range(n)])
		    left_point = set([(x, 0) for x in range(m)])
		    right_point = set([(x, n-1) for x in range(m)])
		    bfs(top_point, m, n, matrix)
		    bfs(left_point, m, n, matrix)
		    bfs(bottom_point, m, n, matrix)
		    bfs(right_point, m, n, matrix)
		    result = top_point & left_point & right_point & bottom_point
		    return result
		
		
		if __name__ == '__main__':
		    matrix = [
		        [1, 3, 2, 3, 5],
		        [3, 4, 5, 6, 3],
		        [2, 7, 4, 3, 3],
		        [5, 2, 2, 3, 1]
		    ]
		    print(solve(matrix))
		```
- 运行结果
	- ![](https://img-blog.csdnimg.cn/20190409182233285.png)
- 补充说明
	- 具体代码可以查看我的Github，欢迎Star或者Fork
	- 参考书《你也能看得懂的Python算法书》