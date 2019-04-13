# 八皇后问题
- 简介
	- 回溯法的经典问题。
- 问题描述
	- 有8*8=64个格子，每个格子里面可以放一个棋子，现在要求任意两个棋子不在一条横向、纵向或者斜向的直线上。
- 问题分析
	- 显然，每一行、每一列都只有一个棋子才有可能满足答案要求。
	- 现在，对于这个矩阵，按照行去摆放棋子，第一行只能有一个，假设其在(0,0)的位置，但是现在无法判断棋子在这个位置是否合适，因为后面的棋子都没有确定。所以只能继续假设下去，假设第二行棋子在(1,2)的位置，第三个棋子在(2,4)的位置...如此一直假设下去，最终会有两种结果。
		- 成功假设到了第八行，也就是说，找到了答案之一。
		- 还没到第八行，走不下去了，陷入死局。
	- 如果是第一种结果，那么太好了，输出结果就好了。但是，如果是第二种情况，则需要退一步，重新假设前一行棋子的位置。必要时候，回退到第一行，重新假设第一个棋子位置。
	- 整体思路就是，以第一行为起点，假设棋子位置，目标是能够一直成功假设出有效的第八行棋子的位置，如果中途出现死局，那么改变上一行棋子的位置。
- 代码
	- ```python
		# -*-coding:utf-8-*-
		class Solution(object):
		    def __init__(self):
		        self.result = 0
		
		    def NQueens(self, n):
		        self.helper([-1]*n, 0, n)
		
		
		    def helper(self, column_positions, row_index, n):
		        if row_index == n:
		            # 成功排布到了第n行
		            self.result += 1
		            self.print_solution(column_positions, n)
		            return
		        for column in range(n):
		            # 假设棋子位置
		            column_positions[row_index] = column
		            if self.is_valid(column_positions, row_index):
		                self.helper(column_positions, row_index+1, n)
		
		    def is_valid(self, column_positions, row_index):
		        """
		        判断当前棋盘是否合适
		        :param column_positions:
		        :param row_index:
		        :return:
		        """
		        for i in range(row_index):
		            if column_positions[i] == column_positions[row_index]:
		                # 同列
		                return False
		            elif abs(column_positions[i] - column_positions[row_index]) == row_index - i:
		                # 同斜
		                return False
		        return True
		
		    def print_solution(self, column_positions, n):
		        """
		        格式化输出棋盘方案
		        :param column_positions:
		        :param n:
		        :return:
		        """
		        for row in range(n):
		            line = ""
		            for column in range(n):
		                if column_positions[row] == column:
		                    line += "Q"
		                else:
		                    line += "."
		            print(line)
		        print()
		
		    def get_result(self):
		        return self.result
		
		
		solution = Solution()
		solution.NQueens(8)
		print(solution.get_result())
		```
- 运行结果
	- ![](https://img-blog.csdnimg.cn/20190413145336219.png)
- 补充说明
	- 具体代码可以查看我的Github，欢迎Star或者Fork
	- 参考书《你也能看得懂的Python算法书》
	- 书中错误已经修改