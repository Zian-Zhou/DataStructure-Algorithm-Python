#限制条件：只允许交易一次
#求最大利润
#重点是解法二

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''


#解法一：
'''
就是找到前后相差最大的两个数，他们的差就是最大利润。这么想的直接解法就是暴力遍历，显然不能让人满意。
于是我们换一个思路，但本质还是一样的：

依次遍历每个数，如果是到当前时候卖出股票，那么产生的最大收益一定是当前的价格和之前最低价格之差
因此我们需要记录遍历过程中最低价格，并且遍历过程中都会产生一个收益，保留最大收益，最终遍历完毕就是要找的解。
'''
def maxProfit(prices):
	if len(prices)<2:
		return 0
	minPrice,maxProfit = float('inf'),0
	for price in prices:
		maxProfit = max(maxProfit,price-minPrice)
		minPrice = min(minPrice,price)
		'''
		上面两句的顺序可以调换，原因在于，当我们碰到当前价格比之前最低价格低的时候，
		最大收益是不会变的
		price-minPrice为0，如果此时minPrice先更新的话；否则为负数（总之只有当当前价格低于最低价格的时候，上面第二句话才会有意义）
		'''
	return maxProfit



#解法二(比较重要的一个做法，后面的题目会用到这个思路)
'''
我们直接用两个变量记录，分别为buy、sell
——buy表示当前为买入状态的最大收益
——sell表示当前为卖出状态的最大收益

那么遍历过程中，我们根据下面思路来更新这两个变量：price为当前价格
	buy = max(buy,-price)      ：意思是当前价格为历史以来最低，那么就定这个为买入价格
	                             -price就表示手头上买入一只股票之后收益为负
	sell = max(sell,buy+price) ：意思是当前价格减去之前买入的价格之后，比之前处于卖出状态的最大收益还要大，就更新sell
								 +price就表示当前价位卖出股票
其实可以发现buy就是解法一中的-minPrice，而sell就是解法二中的maxProfit
'''
def maxProfit(prices):
	if len(prices)<2:
		return 0
	buy=sell=float('-inf')
	for price in prices:
		buy = max(buy,-price)
		sell = max(sell,buy+price)
	return sell