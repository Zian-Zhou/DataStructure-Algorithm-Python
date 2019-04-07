#309. 最佳买卖股票时机含冷冻期

'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''

#动态规划
'''
dp1[i]:第i天手上有股票的最大收益
dp2[i]:第i天手上没有股票的最大收益

那么，dp2[i]有两种可能，一种是第i天卖出股票，即dp1[i-1]+price[i]，表示为第i-1天还持有股票
					   一种是第i-1天就没有持有股票，即dp2[i-1]
					   两种情况取最大值即为第i天手上没有股票的最大收益

	 dp1[i]有两种可能，一种是第i-1天手上已经持有股票，即dp1[i-1],
	 				   一种是第i天买入股票，此时情况复杂一点，因为有冷冻期的存在，因此要求
						第i-1天没有卖出股票的操作，这和第i-1天没有持有股票并不等价，而是和
						第i-2天没有持有股票等价，此时一定过了冷冻期可以买入股票，即dp2[i-2]-price[i]
注意一下初始化即可，dp2全部初始化为0，而dp1[0]初始化为-price[0]
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)<=1:
        	return 0
        l = len(prices)
        dp1 = [0 for _ in range(l)]
        dp2 = [0 for _ in range(l)]
        dp1[0] = prices[0]
        for i in range(1,l):
        	dp2[i] = max(dp1[i-1]+prices[i],dp2[i-1])
        	temp = 0 if i==1 else dp2[i-2]
        	dp1[i] = max(dp1[i-1],temp-prices[i])
        return dp2[-1]

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 引入辅助数组sells和buys
        # sells[i]表示在第i天不持有股票所能获得的最大累计收益
        # buys[i]表示在第i天持有股票所能获得的最大累计收益
        
        n = len(prices)
        if n < 2:
            return 0
        sells = [0] * n
        buys = [0] * n
        sells[0], sells[1] = 0, max(0, prices[1] - prices[0])
        buys[0], buys[1] = -prices[0], max(-prices[0], -prices[1])
        for i in range(2, n):
            sells[i] = max(sells[i-1], buys[i-1] + prices[i])
            buys[i] = max(buys[i-1], sells[i-2] - prices[i])
        return sells[-1]
'''