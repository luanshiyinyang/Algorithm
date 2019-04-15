# -*-coding:utf-8-*-

d = [0.05, 0.1, 0.2, 0.5, 1, 2]
d_sum = [2, 3, 4, 5, 6, 4]
sum_value = 0
for i in range(len(d)):
    sum_value += d_sum[i] * d[i]
input_value = 2.5
if input_value > sum_value:
    print("cannot change")
else:
    i = 5
    while i >= 0:
        if input_value >= d[i]:
            n = int(input_value/d[i])
            if n >= d_sum[i]:
                n = d_sum[i]
            input_value -= n * d[i]
            print("使用了{}个{:.2f}".format(n, d[i]))
        i -= 1
