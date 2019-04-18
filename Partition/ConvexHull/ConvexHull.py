# -*-coding:utf-8-*-
from math import sqrt
solution = []


def convex_hull(points: list):
    if len(points) <= 3:
        return points
    global solution
    points.sort(key=lambda x:x[0])  # 按照横坐标排序
    left_most = points[0]
    right_most = points[-1]
    solution.extend([left_most, right_most])

    helper(points, left_most, right_most, True)
    helper(points, left_most, right_most, False)
    return solution


def helper(points, left_most, right_most, upBool):
    """

    :param points:
    :param left_most:
    :param right_most:
    :param upBool: 上包为True
    :return:
    """
    global solution
    if len(points) <= 1:
        return
    l = line_helper(left_most, right_most)
    if upBool:
        up = []
        max_distance = 0
        max_point = ()
        for point in points:
            distance = 0-(l[0]*point[0]+l[1]*point[1]+l[2]) / sqrt(l[0]*l[0]+l[1]*l[1])  # 与直线的距离
            if distance > 0:
                up.append(point)
                if distance > max_distance:
                    max_distance = distance
                    max_point = point
        if max_point != ():
            solution.append(max_point)
        helper(up, left_most, max_point, True)
        helper(up, max_point, right_most, True)
    else:
        down = []
        min_distance = 0
        min_point = ()
        for point in points:
            distance = 0 - (l[0] * point[0] + l[1] * point[1] + l[2]) / sqrt(l[0] * l[0] + l[1] * l[1])  # 与直线的距离
            if distance < 0:
                down.append(point)
                if distance < min_distance:
                    min_distance = distance
                    min_point = point
        if min_point != ():
            solution.append(min_point)
        helper(down, left_most, min_point, False)
        helper(down, min_point, right_most, False)


def line_helper(point1, point2):
    """
    计算距离
    :param point1:
    :param point2:
    :return:
    """
    if (point1[0]-point2[0]) != 0:
        m = (point1[1]-point2[1]) / (point1[0]-point2[0])
        c = point1[1] - m * point1[0]
        return [m, -1, c]
    else:
        return [1, 0, point1[0]]


if __name__ == '__main__':
    input_points = [(0, 0), (0, 4), (-4, 0), (5, 0), (0, -6), (1, 0)]
    print("Input:", input_points)
    rst = convex_hull(input_points)
    print("Output", rst)

