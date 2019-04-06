# -*-coding:utf-8-*-
class TreeNode:
    def __init__(self, x, l, r):
        self.value = x
        self.left = l
        self.right = r


def get_value(root):
    rst = search(root)
    return max(rst[0], rst[1])


def search(root):
    """
    返回二维数组[偷值，不偷值]
    :param root:
    :return:
    """
    if root is None:
        return [0, 0]
    left = search(root.left)
    right = search(root.right)
    rob_value = root.value + left[1] + right[1]
    skip_value = max(left[0], left[1]) + max(right[0], right[1])
    return rob_value, skip_value


if __name__ == '__main__':
    f = TreeNode(1, None, None)
    e = TreeNode(3, None, None)
    d = TreeNode(1, None, None)
    b = TreeNode(4, d, e)
    c = TreeNode(5, f, None)
    a = TreeNode(3, b, c)
    print(get_value(a))
