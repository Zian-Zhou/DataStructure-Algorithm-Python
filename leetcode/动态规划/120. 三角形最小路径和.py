#120. 三角形最小路径和

'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''

#动态规划
'''
题目是从上到下，其实从下到上也可以求出解。从倒数第二层开始，每一层到达某个位置的路径和，跟到达其下方
相邻的两个位置的路径和有关（取较小的那个）
因此动态规划我们对原来的二维数组直接修改，从倒数第二层开始，计算最小路径和，最终到顶层，就要要求的最小路径
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        n = len(triangle)
        if n==1:
            return triangle[0][0]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
                