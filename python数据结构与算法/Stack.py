#栈 Stack

'''
初始化实例：Stack([1,2,3,4])
'''

class Stack(object):
	def __init__(self,myList):
		'''
		栈顶对应list末元素
		'''
		assert (isinstance(myList,list)), '[Error]: input is not a list.'
		self.stack = myList
		self._size = len(myList)

	#----------------------对外用户接口----------------------
	#value入栈
	def push(self, value):
		self._size += 1
		self.stack.append(value)

	#出栈
	def	pop(self):
		if self.empty():
			print('stack is empty, cannot remove.return is None.')
			return None
		self._size -= 1
		return self.stack.pop()

	#取顶元素
	def top(self):
		if self.empty():
			print('stack is empty, cannot get top.return is None.')
			return None
		return self.stack[-1]

	def empty(self):
		if self._size == 0:
			return True
		else:
			return False

	def size(self):
		return self._size