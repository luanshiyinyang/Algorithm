# 二叉树路径遍历
- 简述
	- 比较基础的一个DFS的题目，但是确实很多难题的模板。LeetCode很多二叉树的题本质上就是这个路径遍历。
	- 本题为了输出路径，使用DFS的经典结构栈完成。
- 问题描述
	- 给定一个二叉树结构（通过类定义节点及父子关系），输出所有到达叶子节点的路径。（二叉树只是标准二叉树）
- 问题分析
	- 明显的遍历题，那么是何种遍历呢？显然，优先的是到达叶子节点而不是辐射更大的范围，这是一个深度优先遍历，遍历完了一个方向找不到路了，则回头遍历其他路径。
	- ![](https://img-blog.csdnimg.cn/20190408143257982.png)
	- 假设对上图的二叉树路径遍历。
		- 我们利用一个stack，里面存放一个Node对象和到这个节点为止的路径（不包括这个节点自己的值）。同时用一个列表res记录所有的路径。
		- 只要栈内还有元素就一直遍历。
			- 每次得到栈顶元素并将其出栈，得到这个Node对象及其路径字符串ls。
				- 若该节点的左右孩子均不存在，这个节点是一个叶子节点。那么将之前的路径加上当前节点的值，作为结果添加到结果集res中。
				- 若该节点的左孩子存在，那么其必然不是孩子节点，将左孩子及加上当前节点值的路径ls入栈。
				- 若该节点的右孩子存在，同上。
		- 当栈空时退出循环，此时res存着所有路径。
- 代码
	- ```python
		# -*-coding:utf-8-*-
		
		
		class Node(object):
		    def __init__(self, x, y, z):
		        self.val = x
		        self.left = y
		        self.right = z
		
		
		def search(root):
		    if not root:
		        return []
		    res, stack = [], [(root, "")]
		    while stack:
		        node, ls = stack.pop()
		        if not node.left and not node.right:
		            res.append(ls + str(node.val))
		        if node.left:
		            stack.append((node.left, ls + str(node.val) + "--->"))
		        if node.right:
		            stack.append((node.right, ls + str(node.val) + "--->"))
		    return res
		
		
		if __name__ == '__main__':
		    d = Node(0, None, None)
		    e = Node(1, None, None)
		    f = Node(1, None, None)
		    b = Node(1, None, d)
		    c = Node(1, e, f)
		    a = Node(0, b, c)
		    print(search(a))
		
		```
- 运行结果
	- ![](https://img-blog.csdnimg.cn/20190408145526960.png)
- 补充说明
	- 具体代码可以查看我的Github，欢迎Star或者Fork
	- 参考书《你也能看得懂的Python算法书》