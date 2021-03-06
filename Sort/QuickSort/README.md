# 快速排序
- 性质
	- 一种基本的交换排序算法，比较常用的排序算法，简称快排。
- 排序思路
	- 基本思想为：通过一趟排序将要排序的数据分割成独立的两部分，分割点左边的数都比它小，分割点右边的数都比它大，然后再按照这个方法对两部分数据进行排序，显然这是一个递归过程。
- 算法详解
	- 待排序列为2,4,5,1,3。
	- 第一步，确定两个指针分别指向序列第一个元素为left和序列最后一个元素为right，并且首先指定第一个数为参考元素base。（left指向2，right指向3，base指2）
	- 第二步，从右至左扫描，偏移right指针，寻找比base小的元素，找到后将其值赋值给left指针。（找到比base小的数值为1，将其赋值给left位置，此时序列变为1,4,5,1,3）
	- 第三步，从左至右扫描，偏移left指针，寻找比base大的元素，找到后将其值赋值给right指针。（找到比base大的数值4，将其赋值给right，此时序列为1,4,5,4,3）
	- 第四步，不断重复二三两步，直到left和right指针位置重合，此时所有元素均被扫描了一遍，将base值赋值给重合的位置。此时，已经完成了一轮排序，base（2）左边都是比它小的，右边都是比它大的。（此时序列为1,2,5,4,3）
	- 第五步，以base数为分割点，两侧分别进行前四步。递归下去，完成排序。
- 算法分析
	- 复杂度
	
		| 排序名称 | 最好情况 | 最坏情况 | 平均情况 |
		| :---: | :---: | :---: | :---: |
		| 快速排序 | O(nlogn) | O(n^2) | O(nlogn) |

	- 当数据有序时，以第一个关键字为分割点，一边为空，效率最差。
	- 数据随机分布，左右数量相当，效率最好。
	- 显然，数据越随机分布，快排效果越好，越接近有序，效果越差。
	- 快排相同元素可能交换位置，所以是不稳定的排序。