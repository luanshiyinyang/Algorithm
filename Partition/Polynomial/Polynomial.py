# -*-coding:utf-8-*-
from cmath import pi, exp


def FFT(A, w):
    length = len(A)

    if length == 1:
        return [A[0]]

    A_even = []
    A_odd = []
    for i in range(0, length // 2):
        A_even.append(A[2 * i])
        A_odd.append(A[2 * i + 1])
    F_even = FFT(A_even, w ** 2)
    F_odd = FFT(A_odd, w ** 2)
    x = 1
    values = [0 for i in range(length)]
    for i in range(0, length // 2):
        values[i] = F_even[i] + x * F_odd[i]
        values[i + length // 2] = F_even[i] - x * F_odd[i]
        x = x * w
    return values


def solver(A, B):
    length = len(A) + len(B) - 1
    n = 1
    while 2 ** n < length:
        n += 1
    length = 2 ** n
    A.extend([0 for i in range(length - len(A))])
    B.extend([0 for i in range(length - len(B))])

    w = exp(2 * pi * 1j / length)
    A_values = FFT(A, w)
    B_values = FFT(B, w)
    C_values = [A_values[i] * B_values[i] for i in range(length)]
    result = [int((x / length).real) for x in FFT(C_values, w ** -1)]

    while result[-1] == 0:
        del result[-1]
    return result


if __name__ == '__main__':
    input_A, input_B = [3, 2, 3, 4], [2, 0, 1]
    print("A", input_A)
    print("B", input_B)
    result = solver(input_A, input_B)
    print("C", result)
