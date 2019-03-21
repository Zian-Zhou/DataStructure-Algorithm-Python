from BinNode import BinNode
from Queue import Queue
from Stack import Stack
'''
class BinNode:
	def __init__(self, val = None, left = None, right = None):
		self.value = val
		self.lChild = None
		self.rChild = None
'''

class BinTree(object):
	"""docstring for BinTree
	newTree = BinTree()#实例化一棵树，此时根节点，左孩子，右孩子均为None
	newTree.reConstructBinTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])#重构二叉树，自此构成一棵树
	
	可用接口：
	1.newTree.preOrder() - 先序遍历
	2.newTree.inOrder() - 中序遍历
	3.newTree.postOrder() - 后续遍历
	4.newTree.levelOrder() - 层序遍历
	4.newTree.print_tree_list() - 输出一棵树，以list of lists的形式：【root，【...】，【....】】

	"""
	def __init__(self):
		'''
		rootNode: 一个BinNode实例
		'''
		#self._size = 0
		self.root = None
		self.lChild = None
		self.rChild = None

	def insertAsLC(self, newNode):
		self.lChild.insertAsLC(newNode)

	def insertAsRC(self, newNode):
		self.rChild.insertAsRC(newNode)

	#自定义遍历操作
	def visit(self, x):
		print(x)

	#------------------------------各种遍历接口：-------------------------------
	#关于遍历：
	'''
		先说明一下为什么遍历要写迭代算法。虽然递归语法简单，也符合人的逻辑，直观，并且理论上算法复杂度也是
	和迭代版本的算法复杂度在渐近意义上一样，但在实际中并不是如此————这是由于递归的实现也是由栈实现的，这
	样在O(1)操作上的差别就完全不一样了，明显迭代算法在实际上更优
	'''

	#=======================1.先序遍历

	def preOrder(self):
		#self._preOrder_recc(self.root)#递归版本
		self._preOrder_iter(self.root)#迭代版本

	# 迭代版本：利用栈的特性，先进后出
	'''
	宏观上看：
			从根节点开始，总是沿着左侧链下行，并且每次下行都会进行访问（下行一次就碰到根节点，根据先序的定
			义，一定是先访问 visit），同时将当前结点的右孩子压入栈中，直到下行到底部。
			从底部开始，也就是辅助栈依次出栈，继续访问出栈的结点（此时依旧时沿其左侧链访问并下行）

	总结来说，就是每次都沿左侧链下行，依次先访问再入栈。到底部，依次出栈，并重复操作。
	'''
	def _preOrder_iter(self, thisNode):
		S = Stack([])#初始化一个辅助栈
		while(True):
			self._visitAlongLeftBranch(thisNode, S)#遍历当前结点的左侧链
			if(S.empty()):
				break#栈空则结束
			thisNode = S.pop()#弹出下一子树的根

	def _visitAlongLeftBranch(self, thisNode, stack):
		'''
		沿根节点的左侧链，边访问visit，边下行
		rootNode: 结点类
		stack:	  栈类
		'''
		while(thisNode):#遍历左侧链
		#rootNode非空，直到访问到哨兵，也就是说左孩子不存在时
			self.visit(thisNode.value)#访问当前结点的值
			stack.push(thisNode.rChild)#右子树（的根节点）入栈
			thisNode = thisNode.lChild

	# 递归版本:
	def _preOrder_recc(self, root):
		if root==None:
			return
		self.visit(root.value)
		#print(self.root.value)
		self._preOrder(root.lChild)
		self._preOrder(root.rChild)

	#=====================2.中序遍历 
	
	def inOrder(self):
		#self._inOrder_recc(self.root)#递归版本
		self._inOrder_iter(self.root)

	def _goAlongLeftBranch(self, thisNode, stack):
		'''
		沿左侧链下行，并将沿途碰到的结点依次入栈
		'''
		while(thisNode):#当前结点非None，直到为None，即碰到哨兵（左孩子不存在）
			stack.push(thisNode)
			thisNode = thisNode.lChild

	# 迭代版本
	'''
	宏观上看：
			从根节点开始，总是沿着左侧链下行，和先序遍历不同的是，此时并不访问当前的结点，而仅仅
			是入栈当前结点。真正的访问是在出栈的时候，弹出的结点，才进行访问（中序遍历的定义就是先
			访问左孩子，接着才是访问根节点）。
			也就是说，每次访问一定是从左侧链的最低端开始；
			访问完后再进入右孩子，并且再次沿左侧链下行，依次入栈，再次从其左侧链底部开始访问。

	总结来说，就是每次都是沿左侧链下行，先依次入栈，直到底部时再开始出栈。出栈时先访问，再重复前面操作。
	'''
	def _inOrder_iter(self, thisNode):
		S = Stack([])
		while(True):
			self._goAlongLeftBranch(thisNode, S)
			if (S.empty()):
				break
			thisNode = S.pop()
			self.visit(thisNode.value)
			thisNode = thisNode.rChild

	#递归版本
	def _inOrder_recc(self, root):
		if root==None:
			return
		self._inOrder(root.lChild)
		self.visit(root.value)
		self._inOrder(root.rChild)

	#==============================3.后序遍历
	def postOrder(self):
		#self._postOrder_recc(self.root)# 递归版本
		self._postOrder_iter(self.root)# 迭代版本 待完成

	# 迭代版本
	'''
	这个迭代算法比较难想，要多加揣摩。。。还没完成。。。。有bug（有另外一种实现方式：用两个辅助栈实现）
	大概思路就是用一个栈存所有的结点，并且保证栈顶元素要么是当前结点的父亲，要么是当前结点的右兄弟
	这样访问完当前结点，就要执行弹出栈的操作，得到的结点一定是先右结点
	其次是保证，每次入栈的顺序，一定要是父节点先入栈，右孩子再入栈，接着左孩子入栈，然后继续沿着左孩子下行
	'''

	def _gotoHLVFL(self, stack):
		while(True):
			thisNode = stack.top()#当栈顶为空节点的时候，结束循环，并在循环之后，将空节点弹出
			if thisNode is None:#如果栈顶元素为空，结束循环
				break
			thisNode.maskParent += 1
			if thisNode.lChild is not None:#如果当前结点存在左孩子（非空）
				if thisNode.rChild is not None:#并且当前结点存在右孩子
					stack.push(thisNode.rChild)#就把右孩子压入栈中
				stack.push(thisNode.lChild)#然后将当前结点的左孩子压入栈中
			else:#如果当前结点没有左孩子
				stack.push(thisNode.rChild)#将当前结点的右孩子压入栈中（可能为空，但没关系，看下步操作）
		stack.pop()#上面循环结束之后，栈顶一定是空节点，弹出即可（结束条件就是出现空节点。。。）
		

	def _postOrder_iter(self, thisNode):
		S = Stack([])
		if thisNode is not None:#当前结点非空,则入栈
			S.push(thisNode)
		#count = 0
		while(not S.empty()):#循环，直到栈空
			#if S.top().lChild == thisNode or S.top().rChild == thisNode:#如果栈顶结点是当前结点的父亲
			#count+=1
			#print(count)
			if S.top().maskParent==0:#栈顶结点还没开始第一次访问
			#也就是说当前结点访问完后，他的右兄弟还没访问，那就在访问父亲之前访问右结点
				S.top().maskParent += 1#
				self._gotoHLVFL(S)#在当前结点的右子树找到左侧可见的最高叶子
			thisNode = S.pop()#出栈
			self.visit(thisNode.value)#访问

	# 递归版本
	def _postOrder_recc(self, root):
		if root==None:
			return
		self._postOrder_recc(root.lChild)
		self._postOrder_recc(root.rChild)
		self.visit(root.value)

	#=============================4.层序遍历 迭代算法
	def levelOrder(self):
		self._levelOrder(self.root)

	def _levelOrder(self, root):
		Q = Queue([])#初始化空队列
		Q.enqueue(self.root)
		while(not Q.empty()):
			x = Q.dequeue()
			self.visit(x.value)#每次出队就访问

			if x.lChild is not None:#有左孩子则左孩子入队
				Q.enqueue(x.lChild)
			if x.rChild is not None:
				Q.enqueue(x.rChild)

	#----------------------------重构二叉树--------------------------

	#根据中序遍历序列以及先序遍历重构二叉树
	def reConstructBinTree(self, preOrderList, inOrderList):
		if not preOrderList or not inOrderList:
			print('one of the inputs:preOrderList or inOrderList is empty.' )
		if len(preOrderList)!=len(preOrderList):
			print('Cannot build BinTree, since: the two list have different length.')

		self.root = self._reConstructBinTree(preOrderList, inOrderList)
		self.lChild = self.root.lChild
		self.rChild = self.root.rChild

	def _reConstructBinTree(self, preOrderList, inOrderList):
		'''
		#root:当前根节点
		preOrderList:先序遍历序列
		inOrderList:中序遍历序列
		'''
		if not preOrderList or not inOrderList:
			#print('one of the inputs:preOrderList or inOrderList is empty.' )
			return None

		root = BinNode(preOrderList[0],None,None)
		#找到中序遍历序列中对应找到的根节点的位置index，这样其左右分别为左右子树
		val = inOrderList.index(preOrderList[0])#也就是说，preOrderList[val]和inOrderList[val]都对应根节点的值

		root.lChild = self._reConstructBinTree(preOrderList[1:val+1],inOrderList[:val])
		root.rChild = self._reConstructBinTree(preOrderList[val+1:],inOrderList[val+1:])

		return root

	#----------------------------输出一棵树---------------------------

	def print_tree_list(self):
		'''
		BinTree().print_tree_list()
		'''
		#print(self._print_tree_list(self.root))
		return self._print_tree_list(self.root)

	def _print_tree_list(self,root):
		'''
		root:当前根节点,目的是递归
		'''

		'''和哨兵的思路作对比，立分高下
		if root.lChild is None and root.rChild is None:
			return [root.value, [None], [None]]
		elif root.lChild is None:
			return [root.value, [None], [self._print_tree_list(root.rChild)]]
		else:
			return [root.value, [self._print_tree_list(root.lChild)], [self._print_tree_list(root.rChild)]]
		'''
		#哨兵，碰到哨兵即回头
		if root is None:
			return None
		return [root.value, [self._print_tree_list(root.lChild)],[self._print_tree_list(root.rChild)]]


