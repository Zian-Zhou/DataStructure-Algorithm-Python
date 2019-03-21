#647-回文字符串

'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
'''

#动态规划
#https://blog.csdn.net/OneDeveloper/article/details/79853156
'''
一个字串如果是回文的，只有下面三种情况：
要么他是单个字符，
要么是两个相同字符组成的，
要么是至少三个字符组成，其首尾字符相同，并且去掉首尾字符的字符串仍然是字符串

这就得到一个递推关系，如果一个字符长度超过2，那么他是否为回文字串取决于首尾字符相不相同以及去掉首尾字符之后
是不是回文的字串。因此所有的大字符串都可以转化成小字符串来求解，用动态规划实现的时候只需要维护一个二维数组dp,
其中dp[i][j]表示字符串的第i个字符到第j个字符组成的字符串是否构成回文的，那么其对角线初始化为True，对角线往右上方
的位置表示相邻两个字符能否组成回文字串，取决于是否相同。初始化完毕之后，沿着左下到右上的方向依次更新斜线的值，
每个元素都与其左下相邻的值以及首尾字符是否相同有关。
注意我们只需要统计二维数组右上角即可
'''

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return False
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count=0
        for i in range(n):
        	dp[i][j]=True
        	count+=1
        for i in range(n-1):
        	if s[i]==s[i+1]:
        		dp[i][i+1]=True
        		count+=1

        for j in range(2,n):
        	for i in range(n-j):
        		if s[i]==s[j+i] and dp[i+1][j+i-1]:
        			dp[i][j+i]=True
        			count+=1
        return count