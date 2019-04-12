# -*-coding:utf-8-*-
# -*-coding:utf-8-*-

result = []


def solve(array, number, solution):
    global result
    if len(solution) == number:
        # 表示所有书都分配完毕，输出答案
        result.append(solution)
        return
    for i in range(len(array)):
        new_solution = solution + [array[i]]
        new_array = array[i+1:]
        solve(new_array, number, new_solution)


if __name__ == '__main__':
    input = ['A', 'B', 'C', 'D']
    solve(input, 2, [])
    for item in result:
        print(item)
    print("共{}种组合".format(len(result)))