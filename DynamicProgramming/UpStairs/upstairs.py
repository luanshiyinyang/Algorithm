def upstairs(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return upstairs(n-1) + upstairs(n-2)


for i in range(1, 11):
    print("到第{}级的方案有{}种".format(i, upstairs(i)))