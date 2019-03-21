#64.最小的路径和

'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''

#解答：
'''
由于只能向下或者只能向右移动一步，因此如果我们用dp[i][j]表示到达第i行第j列的最小路径和，那么它与
它上面的值dp[i-1][j]以及它左边的值dp[i][j-1]有关，我们有递推式：
    dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
而这个二维数组的第一行和第一列中每个元素的值是确定的，只需依次累加即可。因此从行开始遍历，然后依次
遍历列，填补这个二维数组的各个位置的值，最终右下角的值就是要求解的答案。
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        dp = [[0]*cols for _ in range(rows)]
        dp[0][0]=grid[0][0]
        for i in range(1,rows):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,cols):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[rows-1][cols-1]