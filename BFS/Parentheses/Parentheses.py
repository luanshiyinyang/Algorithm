# -*-coding:utf-8-*-
def is_valid(s):
    """
    判断是否括号合法
    :param s:
    :return:
    """
    count = 0
    for item in s:
        if item == "(":
            count += 1
        elif item == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0


def solve(s):
    res = []
    queue = []
    queue.append(s)
    while len(queue) > 0:
        # 每次去队列找其中元素，这时队列里面的都是一层的
        for item in queue:
            if is_valid(item):
                res.append(item)
        if len(res) > 0:
            # 只有这一层没有合法的，才会继续去除括号向下一层找
            return list(set(res))
        temp = []
        for item in queue:
            for i in range(len(item)):
                if item[i] == "(" or item[i] == ")":
                    temp.append(item[:i] + item[i+1:])
        queue = list(set(temp))
    return list(set(res))


if __name__ == '__main__':
    print(solve("(a)(b))()"))
