#95. 不同的二叉搜索树 II
'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

'''
前面一题让我们求不同的BST共有几种，可以用动态规划求解，或者直接求卡特兰数的值。
这里要求输出所有可能的情况，那么就采用dfs，用递归实现
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n or n<=0:
        	return []
        return self.dfs(1,n)


    def dfs(self,start,end):
    	if start>end:#递归返回条件，此时对应的上一递归层是一个数组成的，自然就只有一个节点
    		return [None]
    	res = []
    	for val in range(start,end+1):#遍历从start到end，val分别做节点组成的二叉树
    		leftTree = self.dfs(start,val-1)#val左边的数字属于左子树（下一层递归这是构造不同数字作根节点的左子树）
    		rightTree = self.dfs(val+1,end+1)#右边的数字属于右子树
    		#上面两个返回的是左右子树所有可能的情形，list[root1,root2,...]
    		for l in leftTree:
    			for r in rightTree:
    				root = TreeNode(val)#当前值构造根节点，分别跟上面返回的左右子树所有情形组合成不同的树
    				root.left = l
    				root.right = r
    				res.append(root)
    	return res