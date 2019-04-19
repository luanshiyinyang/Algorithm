# -*-coding:utf-8-*-


class Solution():
    def solveFloyd(self, dist, start, end):  # 核心方法
        n = len(dist)
        path = self.createPath(n)
        for k in range(n):  # 遍历节点，设成中介点
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:  # 如果路程更短
                        dist[i][j] = dist[i][k] + dist[k][j]  # 更新D，P矩阵
                        path[i][j] = path[i][k]
        self.printPath(start, path, end)  # 输出

    def createPath(self, n):  # 创建P矩阵
        path = []  # 一个长度为n，由[0,1,2,3,…,n-1]构成的二维数组
        for i in range(n):
            row = []
            for j in range(n):
                row.append(j)
            path.append(row)
        return path

    def printPath(self, current, path, end):  # 输出方法
        solution = []  # solution为最短路线列表
        while current != end:  # 只要当前节点不为终点
            solution.append(current)  # 把当前节点加入solution
            current = path[current][end]  # 设当前节点为路线中的下一个节点
        solution.append(current)  # 最后加入终点
        print(solution)  # 输出solution
