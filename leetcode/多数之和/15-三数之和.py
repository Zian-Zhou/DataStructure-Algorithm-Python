
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

#解答
'''
https://blog.csdn.net/iyuanshuo/article/details/79600142

要求的是a+b+c=0
其实就是要求a+b=-c，那么问题可以转化为依次遍历数组元素c，然后在剩下的数中做两数之和为-c的问题。

问题在于如何简化算法以及优化复杂度。
	1.首先可以先排序（O(nlogn)），这样保证数组有序之后可以利用大小关系判断。
	2.设置两个指针left、right，分别从左边以及右边向中间遍历，如果找到a+b+c==0，那么可以将这个答案加入到答案集里
		如果a+b+c<0，此时固定的是c，说明a+b太小了，因此left+=1；如果a+b+c>0，此时a+b过大，因此right-=1
	3.去重，这一步则是利用了有序性，如果两个数相同，那他们在数组的位置一定是相邻的（连着几个数相同也是可能的），因此
		去重的操作就能简单遍历一下相邻的是否相同即可。由于数组有序性使得去重这一步很简单，因此也可以看出第一步的作用。

	此外还有一些小细节的地方，比如说当遍历到c>0的时候，由于之后的数都是正数，那三数之和一定大于0，就没必要继续遍历c了(因为
	继续向后遍历c只会更大，那之后的数加起来一定大于0)；
	或者固定c，如果c及其后面连着两个数a,b，他们的和已经大于0了，就没必要进行下一步的操作，此时遍历下一个c；
	同理，如果c和数组最后两个数的和仍然小于0，也没必要进行下一步操作。

'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
        	if nums[i]>0:#排好序之后，如果nums[i]>0，说明后面的数全部大于0
        		break
        	if i==0 or nums[i]>nums[i-1]:#去重	
	        	left,right = i+1,len(nums)-1
	        	#剪枝
	        	if nums[i]+nums[left]+nums[left+1]>0 or nums[i]+nums[right-1]+nums[right]<0:
	        		continue
	        	while left<right:
	        		ident = nums[i]+nums[left]+nums[right]
	        		if ident==0:
	        			res.append([nums[i],nums[left],nums[right]])
	        			left+=1
	        			right-=1
	        			#去重
	        			while left<right and nums[left]==nums[left-1]:
	        				left+=1
	        			while left<right and nums[right]==nums[right+1]:
	        				right-=1
	        		elif ident<0:
	        			left+=1
	        		else:
	        			right-=1
        return res