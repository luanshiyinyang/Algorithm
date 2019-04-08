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
