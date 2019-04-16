# 哈夫曼编码
- 简介
	- 哈夫曼编码是一种字符编码方式，可以对指定的字符集进行数据压缩，压缩率在20%到90%。
- 问题描述
	- 现在有一个包含5个字符{A,B,C,D,E}，各个字符的出现频率依次为{0.35, 0.1, 0.2, 0.2, 0.15}。需要构造一种有效的编码类型，使用该编码表达以上字符表时可以产生平均长度最短的位串。
- 问题分析
	- n个字符组成的文本编码时有两种方式，定长编码（为每个字符赋予一个长度固定为m，m>=log_2^n的位串，ASCII码就是如此的）和变长编码（长度各异的编码，其中出现频率高的采用较短的编码表示，摩斯电吗就是如此做的）。通常，为了提高效率一般使用定长编码，但是定长编码会遇到一个问题，就是前缀码问题。所谓前缀码，就是对任意字符使用01串表示其，并且任何一个字符的编码不是其他字符的前缀。有了前缀码，就可以在位串中准确定位字符，快速替换文本了。
	- 哈夫曼提出来这种编码策略，称为哈夫曼编码。其核心就是利用二叉树这种数据结构。（前缀码是简单路径的节点值得来的，是通过从一个叶子节点到另一个叶子节点的简单路径不存在来保证的。
	- 这样的二叉树称为哈夫曼树，算法如下。
		- 初始化n个单节点的树，并标上字母表中字符。把每个字符的频率记录在对应的根节点中，用来标记树的权重，即树的权重为所有节点的概率和。
		- 重复下面的步骤，直到只剩下一棵单独的树。找到两课权重最小的树，若权重相同，任选其中一个，分别把它们作为新二叉树的左右子树，并将其权重之和作为新的权重记录根节点中。
		- 这样的树就是哈夫曼树，获得树后依据左分支为0，右分支为1，可以得到编码。
	- 对题目的例子，哈夫曼编码节约了25%的存储空间。
	- 对贪心选择性质和最优子结构性质理解不难，这里不做证明了。
- 代码
	- ```python
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
		```
- 运行结果
	- ![](https://img-blog.csdnimg.cn/20190416213252869.png)
- 补充说明
	- 具体代码可以查看我的Github，欢迎Star或者Fork
	- 参考书《你也能看得懂的Python算法书》