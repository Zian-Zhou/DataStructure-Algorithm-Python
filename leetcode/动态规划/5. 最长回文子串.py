# 5. 最长回文子串

#动态规划
'''
dp[i][j]表示字符串从第i个字符到第j个字符组成的子串是否回文，是则为1，不是则为0
这样当i==j时，dp[i][j]=1; 当i+1==j时，如果s[i]==s[j]，则dp[i][j]==1;
当i+1<j时，如果s[i]==s[j]，dp[i][j]=dp[i+1][j-1]（比如'aba'——>'b'）
这样用二维数组记录动态规划的过程就是从对角线开始向右上角按斜线更新，显然越靠右上方的i,j相距越远，
也就是说，最终的结果中dp为1的位置最靠右上方的就是长度最长的子串。
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s)<=1:
        	return s
        l = len(s)
        dp = [[0]*l for _ in range(l)]
        for i in range(l):
        	dp[i][i]=1
        left=right=0
        for i in range(1,l):
        	if s[i-1]==s[i]:
        		dp[i-1][i]=1
        		left = i-1
        		right = i
        for j in range(2,l):
        	for i in range(l-j+1):
        		if s[i]==s[j+i] and dp[i+1][j+i-1]:
        			dp[i][j+i]=1
        			left = i
        			right = j+i
        return s[left:right+1]