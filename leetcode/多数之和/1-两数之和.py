



'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
#https://blog.csdn.net/linfeng886/article/details/79772348


#暴力法
def twoSum(nums,target):
	l = len(nums)
	for i in range(l):
		for j in range(i,l):
			if nums[i]+nums[j]==target:
				return [i,j]



#解答：
'''
利用哈希表降低时间复杂度，只需要遍历一次就可以找到[i,j]

采用一个词典存储访问过的值及其对应的下标，在遍历过程中判断当前数值与target的差值是否在之前访问过了，如果访问过，说明
我们找到了一对答案，那就根据字典键值对得到对应下标；如果没有访问过，那就更新字典中当前数值的下标。
'''
def twoSum(nums.target):
	d = {}
	for i,num in enumerate(nums):
		if target-num in d:
			return [d[target-num],i]
		else:
			d[num]=i 