#似乎是剑指offer第二版原题吧？

'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：

你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：

你能在线性时间复杂度内解决此题吗？
'''

#解答：
'''
可以用一个队列存储滑动窗口里面对应的下标，要保证队头为当前窗口最大值的下标。因此遍历过程中入队出队需要满足下面的要求：
    1.入队：从队尾入队，首先如果入队的数要大于队尾对应元素，那么就要将队尾元素移除（即从尾端出队）
            因此这是一个循环操作，直到队尾元素对应的值比要入队的数大时，或者队列变空，方可入队
    2.出队：由于队列存储滑动窗口里面对应的下标，那么要保证队头元素（下标）在滑动窗口的下标中，此时当下标超过滑动窗口
            时，就要从队头移除这个下标。

因此我们要采用双向队列来实现。下面的代码中使用了list来模拟，由于有list.pop(0)操作，这个操作是O(n)复杂度的。所以如果要
优化的话，建议实现一个双向队列（双向链表）。反正我如果使用collections模块里面的deque的话，发现居然不支持判断empty()还
有访问队首以及队尾元素的top()接口。。。
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return None
        Q = []
        res = []
        currentIndex=0
        while currentIndex<len(nums):
            if len(Q)>0 and currentIndex-Q[0]>=k:
                #Q=Q[1:]
                Q.pop(0)
            while len(Q)>0 and nums[currentIndex]>nums[Q[-1]]:
                Q.pop()
            Q.append(currentIndex)

            if currentIndex>=k-1:
                res.append(nums[Q[0]])
            currentIndex+=1
        
        return res