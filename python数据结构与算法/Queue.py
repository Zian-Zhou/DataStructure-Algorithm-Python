#队列 Queue

'''
初始化实例：Queue([1,2,3,4])
python里面自带queue
这里自己尝试实现一下
'''

class Queue(object):
	"""docstring for Queue"""
	def __init__(self, myList):
		'''
		myList: 输入一个list，得到一个队列Queue

		首元素对应首元素，末元素对应末元素
		'''
		assert (isinstance(myList,list)), '[Error]: input is not a list.'
		self.queue = myList
		self._size = len(myList)

	#----------------------------对外用户接口-------------------------
	def enqueue(self, newValue):
		'''
		新元素入队，加入到末端
		'''
		self._size += 1
		self.queue.append(newValue)

	def dequeue(self):
		'''
		出队
		'''
		if self.empty():
			print('cannot dequeue since queue is empty.return None')
			return None
		self._size -= 1
		return self.queue.pop(0)

	def front(self):
		if self.empty():
			print('queue is empty.return None')
			return None
		return self.queue[0]

	def empty(self):
		if self._size:#非空
			return False
		else:#空队列
			return True

	def size(self):
		return self._size