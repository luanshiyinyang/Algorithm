# -*-coding:utf-8-*-

result = []


def solve(array, solution):
    global result
    if len(array) == 0:
        # 表示所有书都分配完毕，输出答案
        result.append(solution)
        return
    for i in range(len(array)):
        new_solution = solution + [array[i]]
        new_array = array[:i] + array[i+1:]
        solve(new_array, new_solution)


if __name__ == '__main__':
    input = ['A', 'B', 'C', 'D']
    solve(input, [])
    for item in result:
        print(item)
    print("共{}种排列".format(len(result)))