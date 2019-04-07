#764. 最大加号标志

'''
https://leetcode-cn.com/problems/largest-plus-sign/

在一个大小在 (0, 0) 到 (N-1, N-1) 的2D网格 grid 中，除了在 mines 中给出的单元为 0，
其他每个单元都是 1。网格中包含 1 的最大的轴对齐加号标志是多少阶？
返回加号标志的阶数。如果未找到加号标志，则返回 0。

一个 k" 阶由 1 组成的“轴对称”加号标志具有中心网格  grid[x][y] = 1 ，
以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。
下面给出 k" 阶“轴对称”加号标志的示例。
注意，只有加号标志的所有网格要求为 1，别的网格可能为 0 也可能为 1。

阶 1:
000
010
000

阶 2:
00000
00100
01110
00100
00000

阶 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
'''

#动态规划
'''
https://blog.csdn.net/fuxuemingzhu/article/details/82725695
一个比较容易理解的方法就是，我们先确定一个dp数组，
这个数组dp[i][j]保存的是到从i,j位置向上下左右四个方向能拓展的长度。
最后每个位置能拓展多远就是上下左右四个方向能拓展长度的最小值。
我选择遍历的方向是左右上下，那么到下的遍历的时候，dp数组保存的就就是最小的边长了。

这个题四个方向是对称的，因此只需要知道一个方向怎么写，那么直接改循环方向就行，
根本不用思考我查找的方向到底是四个方向中的哪一个。同时使用了set把二维坐标改成了一维，可以加快查找。

时间复杂度是O(n^2)，空间复杂度是O(n^2).
'''
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        if not N or N<=0:
        	return 0
        res = 0
        s = set()
        for m in mines:
        	s.add(m[0]*N+m[1])
        dp = [[0]*N for _ in range(N)]
        for i in range(N):#遍历每行
        	count = 0
        	j = 0
        	while j<N:#从右到左遍历
        		count = 0 if N*i+j in s else count+1
        		dp[i][j] = min(dp[i][j],count)
        		j+=1
        	count = 0
        	while j>0:#从左到右遍历
        		j-=1
        		count  = 0 if N*i+j in s else count+1
        		dp[i][j] = min(dp[i][j],count)

        for j in range(N):#遍历每列
        	count = 0
        	while i<N:#从上到下遍历
        		count = 0 if N*i+j in s else count+1
        		dp[i][j] = min(dp[i][j],count)
        		i+=1
        	while i>0:#从下到上遍历
        		i-=1
        		count = 0 if N*i+j in s else count+1
        		dp[i][j] = min(dp[i][j],count)
        		res = max(dp[i][j],res)
        return res