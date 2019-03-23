def gold_mining(n ,w, G, P):
    """
    利用递归实现动态规划算法过程
    :param n:
    :param w:
    :param G:
    :param P:
    :return:
    """
    if n <= 1 and w < P[0]:
        return 0
    if n == 1 and w >= P[0]:
        return G[0]
    if n > 1 and w < P[n-1]:
        return gold_mining(n-1, w, G, P)
    if n > 1 and w >= P[n-1]:
        return max(gold_mining(n-1, w, G, P), gold_mining(n-1, w-P[n-1], G, P) + G[n-1])


if __name__ == '__main__':
    G = [400, 500, 200, 300, 350]
    P = [5, 5, 3, 4, 3]
    n = 5
    w = 10
    print(gold_mining(n, w, G, P))