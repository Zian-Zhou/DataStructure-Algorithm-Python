
'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
'''


#解法1：
'''
O(n^2)，i遍历数组，j从i到数组末端遍历，计算i到j这一段子数组的和
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
        	for j in range(i,len(nums)):
        		if sum(nums[i:j+1])==k:
        			count+=1
        return count

#解法二：
'''
发现前面有很多求和计算是大量重叠的。可以考虑类似数列求和（Prefix sum）的想法：
	P[i]=A[0]+A[1]+...+A[i-1]
	P[j]=A[0]+A[1]+...+A[i-1]+...+A[j-1]

	A[i]+...+A[j-1]=P[j]-P[i]
因此我们只需要遍历一遍就可以得到所有的P[i]，自然两两相减就是连续子数组的和。遍历过程中用一个字典记录
P[i]，如果字典里已经有这个值了，那么对应的value就加一，表示到目前为止取值为p[i]有多少个。因为要找的是
p[j]-p[i]=k，因此只要对应字典中找到p[i]=p[j]-k，j表示遍历过程中当前的位置。
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}#如果恰好第一个数就是k，那么做差就为0    
        count = 0
        currSum = 0
        for num in nums:
        	currSum+=num
        	target = currSum-k
        	if target in d:
        		count+=d[target]
        	if currSum in d:
        		d[currSum]+=1
        	else:
        		d[currSum]=1
        return count