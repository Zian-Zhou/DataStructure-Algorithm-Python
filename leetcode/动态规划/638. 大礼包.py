#638. 大礼包

'''
在LeetCode商店中， 有许多在售的物品。

然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。

现给定每个物品的价格，每个大礼包包含物品的清单，以及待购物品清单。请输出确切完成待购清单的最低花费。

每个大礼包的由一个数组中的一组数据描述，最后一个数字代表大礼包的价格，其他数字分别表示内含的其他种类物品的数量。

任意大礼包可无限次购买。

示例 1:

输入: [2,5], [[3,0,5],[1,2,10]], [3,2]
输出: 14
解释: 
有A和B两种物品，价格分别为¥2和¥5。
大礼包1，你可以以¥5的价格购买3A和0B。
大礼包2， 你可以以¥10的价格购买1A和2B。
你需要购买3个A和2个B， 所以你付了¥10购买了1A和2B（大礼包2），以及¥4购买2A。
示例 2:

输入: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
输出: 11
解释: 
A，B，C的价格分别为¥2，¥3，¥4.
你可以用¥4购买1A和2B，也可以用¥9购买2A，2B和1C。
你需要买1A，2B和1C，所以你付了¥4买了1A和1B（大礼包1），以及¥3购买1B， ¥4购买1C。
你不可以购买超出待购清单的物品，尽管购买大礼包2更加便宜。
说明:

最多6种物品， 100种大礼包。
每种物品，你最多只需要购买6个。
你不可以购买超出待购清单的物品，即使更便宜。
'''

#深度优先搜索所有可能的购买方案以求得最优解
'''
先尽可能多的选择能够购买的礼包，然后在一个个单买满足最后的需求
通过递归实现回溯，即回溯到选择另外一种礼包
具体算法思路在代码中给出。
'''
import sys
class Solution(object):
	def __init__(self):
		self.Min = sys.maxsize

	def CanBeChosen(self,offer,needs):
		#判断能否选择某个礼包
		#遍历礼包每个值，如果大于需求对应的商品，那么就肯定不能购买这个礼包
		for i in range(len(offer)-1):
			if offer[i]>needs[i]:
				return False
		return True

	def buyThisOffer(self,offer,needs):
		#购买指定礼包，然后返回剩下的需求needs
		temp = []
		for i in range(len(needs)):
			temp.append(needs[i]-offer[i])
		return temp

	def chooseOffers(self,price,special,needs,money):
		#递归函数实现
		for offer in special:#对每个礼包进行遍历
			if self.CanBeChosen(offer,needs):#如果当前可以购买指定礼包
				newNeeds = self.buyThisOffer(offer,needs)#那么就购买一个指定礼包，并且返回更新后新的需求
				self.chooseOffers(price,special,newNeeds,money+offer[-1])#执行下一层递归，注意money要加上当前礼包的价格
		for i in range(len(needs)):#挑选完礼包之后，对余下的needs进行单独购买
			money += needs[i]*price[i]
		if money<self.Min:#如果找到一个总花费比之前最小的还要小，更新总体最小值
			self.Min=money

	def shoppingOffers(self, price, special, needs):
		"""
		:type price: List[int]
		:type special: List[List[int]]
		:type needs: List[int]
		:rtype: int
		"""
		self.chooseOffers(price,special,needs,0)
		return self.Min

'''
注意，以上算法不是最优的，可以理解成全排列的问题，假设有ABC三种礼包，那么就会多次计算同一种情形：
例如1A1B1C，比如购买顺序是ABC,ACB,BCA,CBA,但是实际上并没有什么购买顺序，因此是组合问题
'''