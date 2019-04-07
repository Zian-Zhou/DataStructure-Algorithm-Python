#96. 不同的二叉搜索树

'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

'''
	二叉搜索树，因此根节点确定下来，其左右子树含有的节点也就确定下来了。
	比如输入3，取2为根节点，那么左子树就含有1，右子树就含有3.
	因此，给定一个n，取i为根节点，那么1~i-1组成左子树，i+1~n组成右子树，如果记G(n)表示n个数组成BST的可能数，
	那么G(n)=G(0)*G(n-1)+G(1)*G(n-2)+...+G(n-1)*G(0)
	可以用动态规划来求解，注意边界为G(0)=1,G(1)=1；同时这也是卡塔兰数，利用递推公式也可求解
'''

#卡塔兰数解法：
#g(n+1)=2(2n+1)/(n+2)*g(n)
class Solution1(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1:
            return 0
        if n==1:
            return 1
        res = 1
        for i in range(2,n+1):
            res = res*(2*(2*i-1))/(i+1)
        return int(res)
    
#动态规划
class Solution2(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1:
            return 0
        if n==1:
            return 1
        dp = [0]*(n+1)
        dp[0]=1
        for i in range(n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-1-j]
        return dp[-1]
