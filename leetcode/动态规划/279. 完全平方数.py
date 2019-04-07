#279. 完全平方数

'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''

#动态规划
'''
	https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51584790
	
	任何一个数，都可以表示成一个完全平方数加上一个普通的数，即n=i+j*j，
	如果我们记dp[n]表示整数n可以写成完全平和数之和的所需最小个数，那么
	dp[i+j*j]=min(dp[i+j*j],dp[i]+1)
	
	有了递推式我们可以采用动态规划来做，首先初始化dp，每个元素都取一个无穷大的值
	然后所有dp[i*i]都初始化为1，然后从2到n依次根据递推式更新dp各个位置的值，最终
	最后一位的数值就是要求的最终结果
'''
import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        dp = [sys.maxsize]*(n+1)
        i = 0
        while i*i<=n:
            dp[i*i]=1
            i+=1
        for i in range(1,n+1):
            j = 1
            while i+j*j<=n:
                dp[i+j*j]=min(dp[i]+1,dp[i+j*j])
                j+=1
        return dp[-1]

#四平方定理
'''
	https://leetcode-cn.com/problems/perfect-squares/comments/7455
	
	任何一个正整数都可以表示成不超过四个整数的平方之和。
	并且，满足四平方和定理（四个整数），必定满足n=4^a(8b+7)
	因此先判断n能否表示成4个整数的形式，
	接着判断n能否表示成两个整数的情况n=a^2+b^2，当a、b有一个为0的时候返回1，否则返回2，
	如果不能表达成两个整数的情况，那么就返回3
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n%4==0:
        	n/=4
        if n%8==7:
        	return 4
        a = 0
        while a**2<=n:
        	b = int((n-a**2)**0.5)
        	if a**2+b**2==n:
        		return (not not a)+(not not b)
        	a+=1
        return 3
