# 最大的岛屿
- 简介
	- 比较常见的棋盘类型的DFS问题。
- 问题描述
	- 给定一个二维矩阵，其中0代表海洋，1代表陆地（相邻的1连接形成岛屿），现在要求找到最大岛屿面积。
	- 是不是有一种LeetCode的既视感。
- 问题分析
	- 简单暴力的核心思路就是计算每个岛屿的面积，找到最大的即可。
	- 使用从左到右，从上到下的思路遍历矩阵，找到1就说明发现了岛屿，就以岛屿为出发点开始计算面积（根据这个面积决定是否更新最大面积）。
	- 现在的问题就只有，遇到1按照什么规律查看这一整个岛屿呢？显然，由于矩阵的特性以及岛屿的组成规则，可以按照上下左右四个方向进行查找。
	- 深度优先遍历就是这样开始的：从登陆岛屿的第一个位置开始，按照四个方向的规则不断计算岛屿的面积。计算完脚下的，就要走到一个能走的下一个位置，对于下一个位置的选择按照上下左右的顺序进行，知道走到不能走为止。为了不重复计算，增大开销，走过的土地修改为2，标记走过。
- 代码
	- ```python
			# -*-coding:utf-8-*-
			
			
			class Solution(object):
			    def dfs(self, i, j, current_area, grid, max_value=None):
			        # 开始遍历，标记访问
			        grid[i][j] = 2
			        # 向上走可行
			        if i > 0 and grid[i - 1][j] == 1:
			            current_area = self.dfs(i - 1, j, current_area + 1, grid, )
			        if i < len(grid) - 1 and grid[i + 1][j] == 1:
			            current_area = self.dfs(i + 1, j, current_area + 1, grid, )
			        if j > 0 and grid[i][j - 1] == 1:
			            current_area = self.dfs(i, j - 1, current_area + 1, grid, )
			        if j < len(grid) - 1 and grid[i][j + 1] == 1:
			            current_area = self.dfs(i, j + 1, current_area + 1, grid, )
			        self.max_area = max(current_area, self.max_area)
			        return current_area
			
			    def get_max_area(self, grid):
			
			        self.max_area = 0
			        row = len(grid)
			        column = len(grid[0])
			        for i in range(row):
			            for j in range(column):
			                if grid[i][j] == 1:
			                    # 发现陆地
			                    current_area = 1
			                    self.dfs(i, j, current_area, grid, self.max_area)
			        return self.max_area
			
			
			if __name__ == '__main__':
			    grid = [
			        [0, 0, 0, 0, 1, 1, 0],
			        [0, 1, 1, 0, 1, 1, 0],
			        [0, 1, 1, 0, 0, 0, 0],
			        [0, 0, 1, 0, 0, 1, 1],
			        [0, 0, 0, 0, 0, 0, 0],
			        [0, 0, 1, 1, 0, 0, 0],
			        [0, 0, 0, 1, 0, 0, 1]
			    ]
			    print(Solution().get_max_area(grid))
			```
- 运行结果
	- ![](https://img-blog.csdnimg.cn/20190407183901858.png)
- 补充说明
	- 具体代码可以查看我的Github，欢迎Star或者Fork
	- 参考书《你也能看得懂的Python算法书》