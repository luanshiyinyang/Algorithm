# 几何问题之凸包
- 简介
	- 简单地说，凸包是正好包含所有点的凸多边形，可以将它想象为一个包围点几何的橡皮筋。之所以叫凸包是因为这个凸多边形包围所有点。本案例主要讲解分治法解决凸包问题，常见的还有Graham扫描法、Jarvis步进法、快包法等。
- 问题描述
	- 给定点集合，输出凸包的顶点集合。
- 问题分析
	- 分治法讲究分而治之，核心思想很容易理解，难的是想出实施的具体步骤。怎么把大问题拆分成小问题并且确保两者的结构相同，是问题的关键。凸包问题的分治解法不唯一，这里使用其中一种。
	- 步骤
		- 首先，连接最左端和最右端的两点，连接线上方的为上包，下方的为下包。同时，将这两点加入顶点集。
		- 然后，找到直线两侧距离直线最远的两个点，与上一步的两个点相连，此时加入了四条连线，每条连线再次区分上包和下包。这里，将问题分解为4个子问题。新找出的两点肯定是凸包的顶点，将其加入顶点集。
		- 寻找各包中与直线距离最远的点，连接，划分子上包和子下包。直到上包与下包为空，终止循环，输出顶点集合。
	- 总结一下，首先分出上包与下包，然后找两个最远点连线，再次分出两个上包与两个下包。在此之后，上包递归分出两个子上包，下包分出两个子下包，直到包中节点数小于等于1.每一次递归都是把最远点加入顶点集。分治的思路在于每一次递归只找一个顶点，并把剩余顶点交给子问题，也就是子包去解决。
- 代码
	- ```python
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
		
		```
- 运行结果
	- ![](https://img-blog.csdnimg.cn/20190418134635657.png)
- 补充说明
	- 具体代码可以查看我的Github，欢迎Star或者Fork
	- 对代码进行了一些修正
	- 参考书《你也能看得懂的Python算法书