#413. 等差数列划分

'''
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

 

示例:

A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
'''

#解法一：利用等差数列定义以及排列组合思想
'''
	1.n个数排成一排共有n-1个间隔，而等差数列的每个间隔都相等，并且至少为2
	2.假设我们得到连续的n个间隔，那么由这些间隔能够组成的等差数列共有:(n-1)+(n-2)+(n-3)+...+1
	  即共有n*(n-1)/2个
	  其中(n-1)表示两个一组，共有n-1个，而1表示n个一组。
综合1,2，我们只需要先遍历一遍数组，求出每个间隔的值，接着继续遍历这些间隔，找到间隔值相同的最大连续数
然后这个最长的连续数组中利用2可以得到组成的个数，最终找到所有这样的最长连续数组，并求综合既得最终解
'''
class Solution1(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A)<3:
            return 0
        n = len(A)
        tempList = [None]*(n-1)
        for i in range(1,n):
            tempList[i-1]=A[i]-A[i-1]
        res,count = 0,1
        i = 0
        while i<n-2:
            if tempList[i]==tempList[i+1]:
                count+=1
            else:
                res+=count*(count-1)/2
                count=1
            i+=1
        res+=count*(count-1)/2
        return int(res)


#解法二：动态规划
'''
记dp[i]为以第i个数值为结尾的等差数列的个数，那么如果A[i+1]-A[i]==A[i]-A[i-1]，那么第i+1个数结尾的等差数列
个数就是以第i个数值为结尾的等差数列的个数再加上1；如果下一个间隔与当前间隔不相等，则不对dp[i]进行修改。
注意边界情形，dp[0],dp[1]都为0；并且当第一次找到一个间隔相同的时候就已经发现一个长度为3的等差数组，此时就是0+1
因此定义一个长度为n的数组，其上面的值都初始化为0
最终我们要求的总数就是所有dp[i]求和
'''

class Solution1(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A)<3:
            return 0
        n = len(A)
        tempList = [0]*n
        for i in range(2,n):
        	if A[i]-A[i-1]==A[i-1]-A[i-2]:
        		dp[i]=dp[i-1]+1
       	return sum(res)