# 遍历所有的组合方式
- 简介
	- 经典的数学组合问题，对应之前的排列问题。
- 问题描述
	- 现在有四本书为A，B，C，D，要求选出两本，输出所有的选择情况。
- 问题分析
	- 和之前一样，如果试求组合数目，那么**DP**将会是一个不错的选择，但是DP不是很擅长这种序列输出的题。
	- 其实，这还是个回溯题，因为每一步的问题都是一样的只不过参数不一样罢了。
		- 每一步都是在剩余书籍中挑出一本。
		- 与之前的排列问题不同之处在于选过的书本不可以选了，也就是选了AB，B后面的选择就没有A了。
	- 实现与排列类似
- 代码
	- ```python
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
		```
- 运行结果
	- ![](https://img-blog.csdnimg.cn/2019041214371763.png)
- 补充说明
	- 具体代码可以查看我的Github，欢迎Star或者Fork
	- 参考书《你也能看得懂的Python算法书》
	- 书中错误已经修改