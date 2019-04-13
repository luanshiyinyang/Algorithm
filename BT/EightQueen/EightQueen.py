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