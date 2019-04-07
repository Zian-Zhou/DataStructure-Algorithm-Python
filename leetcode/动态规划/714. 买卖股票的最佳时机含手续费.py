#714. 买卖股票的最佳时机含手续费
'''

给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

'''

#解法一：耗时长
'''
动态规划，
dp1记为第i天手上有股票的最大收益
dp2记为第i天手上没有股票的最大收益
因此对于第i天来说，dp1[i]=max(dp1[i-1],dp2[i-1]-prices[i])，第二项表示第i-1天没有股票，而第i天买入股票
				 dp2[i]=max(dp2[i-1],dp1[i-1]+prices[i]-fee)，第二线表示第i-1天有股票，而第i天卖出股票
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices)<=1:
            return 0
        dp1 = [0 for _ in range(len(prices))]
        dp2 = [0 for _ in range(len(prices))]
        
        dp1[0] = -prices[0]
        for i in range(1,len(prices)):
            dp1[i] = max(dp1[i-1],dp2[i-1]-prices[i])
            dp2[i] = max(dp2[i-1],dp1[i-1]+prices[i]-fee)
        return dp2[-1]

#解法二： 耗时短
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        aa = 0

        bb = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<bb:
                bb=prices[i]
            elif prices[i]-bb-fee>0:
                aa+=prices[i]-bb-fee
                bb=prices[i]-fee
  
        return aa