
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

#解答：
'''
建议看T15-三数之和的解答。四数之和相当于固定第一个数，然后求三数之和，而三数之和相当于固定第一个数，求两数之和。
这样问题就简化成如何求两数之和了。搞清楚三数之和的做法以及去重操作的细节，很容易写出四数之和，只需要多套一层循环。
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        l = len(nums)
        nums.sort()
        for i in range(l-3):
            if i==0 or nums[i]>nums[i-1]:#去重
                for j in range(i+1,l-2):
                    if j==i+1 or nums[j]>nums[j-1]:#去重
                        left = j+1
                        right = l-1
                        while left<right:
                            indent = nums[i]+nums[j]+nums[left]+nums[right]
                            if indent==target:
                                res.append([nums[i],nums[j],nums[left],nums[right]])
                                left+=1
                                right-=1
                                while left<right and nums[left]==nums[left-1]:#去重
                                    left+=1
                                while left<right and nums[right]==nums[right+1]:#去重
                                    right-=1
                            elif indent<target:
                                left+=1
                            else:
                                right-=1
        return res
                            
                                