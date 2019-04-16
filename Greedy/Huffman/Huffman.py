# -*-coding:utf-8-*-
class Node(object):
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def is_left(self):
        return self.father.left == self

    def __str__(self):
        return str(self.freq)


def create_nodes(freqs):
    """
    创建叶子节点
    :param freqs:
    :return:
    """
    return [Node(freq) for freq in freqs]


def create_huffman_tree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq+node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


def huffman_encoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.is_left():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes


if __name__ == '__main__':
    chars_freq = [('A', 35), ('B', 10), ('C', 20), ('D', 20), ('E', 15)]
    nodes = create_nodes([item[1] for item in chars_freq])
    root = create_huffman_tree(nodes)
    codes = huffman_encoding(nodes, root)
    for item in zip(chars_freq, codes):
        print('Char:{}freq:{}encoding:{}'.format(item[0][0], item[0][1], item[1]))