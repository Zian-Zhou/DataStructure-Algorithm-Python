class listNode(object):
	def __init__(self, value=None, p=None):
		self.value = value
		self.succ = p


class LinkList(object):
	def __init__(self):
		self._header = listNode()#头结点 哨兵
		self._trailer = listNode()#尾结点 哨兵
		self._size = 0

		self._header.succ = self._trailer
	
	#用于测试输出	
	def printList(self):
		res = []
		if self.empty():
			print(res)
		else:
			pNode = self.first()
			for i in range(self._size):
				if not pNode:
					break
				res.append(pNode.value)
				pNode=pNode.succ
			print(res)

	#按list顺序初始化一个单项链表
	def init_fromList(self,inputList):
		l = len(inputList)
		if l==0:#如果输入的list是[]，直接结束
			return
		#先将list的第一个值接入链表中
		thisNode = listNode(value=inputList[0],p=self._trailer)
		self._size+=1
		self._header.succ = thisNode

		if l>1:
			for i in range(1,l):
				newNode = listNode(value=inputList[i],p=self._trailer)
				thisNode.succ = newNode
				self._size+=1
				thisNode = thisNode.succ

	#基于复制的构造:
	#复制一个链表，从pNode开始的n个后继结点
	def init_copyNodes(self,pNode,n):
		#遍历要复制的链表，依次将结点插入到新链表的尾节点前面
		#这里第一次体现了尾节点的作用
		input_n = n
		while(n>0):
			if not pNode.succ:
				print('n=',input_n,' is out of range after inputNode. Early stopping from copy.')
				return
			self.insertBefore(self._trailer,pNode.value)
			pNode=pNode.succ			
			n -= 1

	def empty(self):
		return not self._size

	#首节点
	def first(self):
		'''
		语义要求：如果链表为空返回None；否则，返回首节点
		'''
		if self._header.succ.value is None:#头结点后继是尾节点：假设实际结点都有具体的值
			print('first():LinkList is empty.Return None!')
			return None
		return self._header.succ

	#寻秩访问
	def call_by_rank(self,rank):
		if self.empty():
			print('call_by_rank:LinkList is empty.Return None!')
			return None
		if rank>=self._size:
			print('call_by_rank:Valid Input: rank is larger than the size of LinkList.Return None!')
			return None
		
		p = self._header.succ#从首节点出发
		while(rank>0):
			p = p.succ
			rank -= 1
		return p.value

	#查找
	def find(self,target,*args):
		'''
		self.find(target,n,pNode) - 在pNode的n个前驱中找到值为target的最后一个节点（仅支持双链）
		self.find(target,pNode,n) - 在pNode的n个后继中找到值为target的第一个结点
		'''
		if isinstance(args[1],int):#在pNode的n个后继中找到值为target的第一个结点
			n = args[1]
			pNode = args[0]

			while(n>0):
				pNode = pNode.succ
				if not pNode:#如果当前结点为空，说明越出了边界
					print('There are less than n nodes after Input Node.Return None!')
					break
				if target == pNode.value:
					return pNode
			return None#如果超出n则查找失败
		else:
			print('only support for doubly linked list!')


	#插入操作:插入结点，首先要创建一个新结点，前驱结点的后继要指向它，并将自身后继指向目标结点

	#在结点p前面插入值为value的节点
	def insertBefore(self,pNode,value):
		'''
		#由于是单项链表，没有前驱指针，因此只能顺序查找，直到找到当前结点的前驱，再执行插入
		插入成功后，返回插入的新节点
		'''
		if not pNode:
			print('Invalid Input. pNode is None')
			return None
		self._size += 1
		newNode = listNode(value=value,p=pNode)#新建一个节点，其后继节点是pNode
		thisNode = self._header
		while(thisNode.succ!=pNode):
			if not thisNode.succ:
				print('Haven found input node in this LinkList.Return None!')
				return None
			thisNode = thisNode.succ
		#如果函数还没有返回，说明此事找到了pNode的前驱结点
		thisNode.succ = newNode
		#newNode.succ = pNode#创建的时候已经实现了

		return newNode

	#在结点pNode后面插入值为value的节点
	def insertAfter(self,pNode,value):
		if not pNode:
			pritn('Invalid Input. pNode is None!')
			return None
		self._size += 1
		newNode = listNode(value=value,p=pNode.succ)#新建结点，其后继是目标结点pNode的后继结点
		pNode.succ = newNode

		return newNode

	#删除节点
	def remove(self, pNode):
		'''
		语义要求：删除合法位置的节点(要求删除的节点一定是链表里面的节点)，返回其数值
		由于是单链，老样子，无法直接得到被删除结点的前驱结点，因此还是要先顺序查找?时间复杂度是O(n)

		真的是这样的吗？其实不然。其实可以将要删除的节点的后继结点删去即可，
		注意此时只需要将后继结点的数值复制到当前结点即可；
		同时要考虑，如果当前结点是尾节点的情况：此时只能顺序查找找到前驱再删除了。
		'''
		'''
		value = pNode.value#备份要返回的数值
		thisNode = self.first()#从首节点开始
		if not thisNode:#如果首结点不在
			return None
		while(thisNode.succ!=pNode):#循环直到找到pNode的前驱结点
			thisNode = thisNode.succ
			if not thisNode:
				print('cannot find inputNode in this LinkList.Return None.')
				return None
		#如果上述循环没有返回，说明此时已经找到了pNode的前驱结点
		thisNode.succ = pNode.succ
		self._size-=1
		del pNode
		return value
		'''
		value = pNode.succ.value
		if value is not None:#如果当前结点不是尾节点,其后继结点的值一定不是None
			pNode.value = value
			delNode = pNode.succ
			pNode.succ = delNode.succ
			del delNode
			self._size-=1
		else:
			value = thisNode.value
			thisNode = self.first()#根据语义，输入的是合法位置的节点，自然要求链表首节点存在
			while(thisNode.succ!=pNode):#循环直到找到pNode的前驱结点
				thisNode = thisNode.succ
			thisNode.succ = pNode.succ
			self._size-=1
			del pNode
		return value

	#去重:删除单链的重复节点
	def deduplitcate(self,sorted=False):
		'''
		语义：如果链表空，返回None；否则去重，并且返回删除结点的个数

		注意到单链是无序的，因此需要遍历一遍链表，找到哪些元素是重复的，再从头开始将每个节点删去
		上述算法可以更改一个思路：遍历一遍链表，用数组记录下哪些元素访问过了，接下来如果碰到相同元素
		（注意这里在辅助数组中查找，如果不借助哈希表，查找的时间复杂度也会影响整体的复杂度）就删去。
		此时需要借助辅助空间，最差需要O(n)空间。不太满意。但是对单链表来说这样也差不多了。。。。
		
		如果是双向链表，就可以采用如下策略：
			遍历链表，保证当前结点之前的节点都是非重复的（不变性），这一步可以采用find接口函数，在当前结点的r个
			前驱中查找相同，如果有相同的，直接删去，如果没有相同的，则继续遍历双向链表。时间复杂度为O(n^2)

		另外，如果链表是有序的，只需要遍历一次就可以解决，时间复杂度O(n),每次找到相同的结点就删去。
		'''
		
		if self.empty():
			print('this LinkList is empty.Return None')
			return None
		if self._size == 1:
			return 0

		#当链表长度大于1时，可能存在重复
		s = {}
		count = 0
		if not sorted:#无序链表
			thisNode = self.first()
			while thisNode.succ:#循环直到当前结点的后继结点为空，就是当前结点是尾节点哨兵
				if thisNode.value in s:#当前结点是重复节点，要删除					count+=1
					self._size -= 1
					thisNode.value = thisNode.succ.value
					delNode = thisNode.succ
					thisNode.succ = delNode.succ
					del delNode
				else:
					s[thisNode.value]=1
					thisNode = thisNode.succ
			#return count
		#如果是有序链表，则可以遍历一次实现,除非被删除结点是尾节点
		else:
			thisNode = self.first()
			nextNode = thisNode.succ

			while(nextNode.value is not None):#循环直到末节点，此时下一节点（尾节点）的值为None
				print('当前结点的值为：{}'.format(thisNode.value),end = ' ')
				print('下一节点的值为：{}'.format(nextNode.value))
				if thisNode.value==nextNode.value:
					count+=1
					thisNode.succ=nextNode.succ
					del nextNode
					self._size-=1
					nextNode = thisNode.succ
				else:
					thisNode=nextNode
					nextNode=nextNode.succ
		
		return count
