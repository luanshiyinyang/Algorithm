# -*-coding:utf-8-*-


class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def solve(root):
    res = []
    queue = []
    queue.append(root)
    while len(queue) > 0:
        # 记录每一层节点数目
        length = len(queue)
        for i in range(length):
            node = queue[0]
            del queue[0]
            if i == length-1:
                res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


if __name__ == '__main__':
    f = Node(7)
    e = Node(5)
    e.left = f
    d = Node(4)
    c = Node(3)
    b = Node(2)
    b.left = d
    b.right = e
    a = Node(1)
    a.left = b
    a.right = c

    print(solve(a))