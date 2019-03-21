

class BinNode:
	def __init__(self, val = None, left = None, right = None):
		self.value = val
		self.lChild = None
		self.rChild = None
		self.maskParent = 0#后序遍历算法

	def insertAsLC(self, newNode):
		'''
		newNode作为当前节点的左孩子插入
		'''
		if self.lChild == None:
			self.lChild = BinNode(newNode.value, newNode.lChild, newNode.rChild)
		else:
			print('original node has lChild')

	def insertAsRC(self, newNode):
		if self.rChild == None:
			self.rChild = BinNode(newNode.value, newNode.lChild, newNode.rChild)
		else:
			print('original node has rChild')



