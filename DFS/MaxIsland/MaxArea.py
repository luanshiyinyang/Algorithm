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
    print("The Islands is")
    for item in grid:
        print(item)

    print("max area is", Solution().get_max_area(grid))