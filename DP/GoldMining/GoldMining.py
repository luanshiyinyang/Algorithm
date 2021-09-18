def gold_mining(n ,w, G, P):
    dp = [0] * (w+1)

    for i in range(1, len(G)+1):
        for j in range(w, 0, -1):
            if j >= P[i-1]:
                dp[j] = max(dp[j], dp[j-P[i-1]] + G[i-1])
    return dp[w]


if __name__ == '__main__':
    G = [400, 500, 200, 300, 350]
    P = [5, 5, 3, 4, 3]
    n = 5
    w = 10
    print(gold_mining(n, w, G, P))
