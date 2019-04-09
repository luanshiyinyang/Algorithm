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