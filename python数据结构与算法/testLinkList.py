#测试单链设计完成的情况：
from LinkList import listNode , LinkList

#初始化空链表
print('-------------------------------')
myList = LinkList()
print('初始化空列表并打印：')
myList.printList()


#按list顺序初始化一个单项链表
print('\n-------------------------------')
print('接口实现：init_fromList,\n按list顺序初始化一个单项链表:')
testList = [1,2,3,4,5]
print('输入List：',testList)
myList.init_fromList(testList)
myList.printList()


#基于复制的构造:
n = 2
print('\n-------------------------------')
print('接口实现：init_copyNodes，\n复制一个链表，从pNode开始的n个后继结点')
print('要复制的链表：',testList,'从第2位开始复制，复制{}个数'.format(n))
inputNode = myList.first().succ
myList2 = LinkList()
myList2.init_copyNodes(inputNode,n)
print('得到的链表为：',end=' ')
myList2.printList()
print('得到链表长度为：',myList2._size)
print('得到链表首节点数值为：',myList2.first().value)


#寻址访问接口测试：
rank = 2
print('\n-------------------------------')
print('接口实现：call_by_rank，\n寻秩访问接口测试：')
print('测试链表：',end=' ')
myList.printList()
print('rank={},返回的值为：{}'.format(rank,myList.call_by_rank(rank)))


#查找接口测试：
target = 4
pNode = myList._header.succ
n = 3
print('\n-------------------------------')
print('接口实现：find,\n查找接口测试： ')
print('测试链表：',end=' ')
myList.printList()
print('在首节点之后的n={}个结点中找到值为target={}的结点'.format(n,target))
print('结点的值为：',myList.find(target,pNode,n).value)


#插入操作接口测试：
value = 10000
value2 = 1111111111111111
target = 4#修改这里的值，可以得到链表对应是这个值的第一个节点
pNode = myList._header
pNode = myList.find(target,pNode,myList._size)
print('\n-------------------------------')
print('接口实现：insertBefore,\n插入接口测试： ')
print('测试链表：',end=' ')
myList.printList()
print('在值为{}的节点之前插入value={}'.format(target,value))
myList.insertBefore(pNode,value)
print('得到的链表为：',end=' ')
myList.printList()

print('在值为{}的节点【后面】插入value={}'.format(target,value2))
myList.insertAfter(pNode,value2)
print('得到的链表为：',end=' ')
myList.printList()
#print(myList._size)


#删除节点操作接口测试：
pNode = myList._header
pNode = myList.find(value2,pNode,myList._size)
print('\n-------------------------------')
print('接口实现：remove,\n删除节点接口测试： ')
print('测试链表：',end=' ')
myList.printList()
print('在链表中删去值为{}的节点'.format(value2))
myList.remove(pNode)
print('得到的链表为：',end=' ')
myList.printList()


#单链去重操作接口测试：
myList3 = LinkList()
myList3.init_fromList([1,1,1,1,1,1,1,2,1,2,3,3,3,4,4,5,5,7,8,9,10,11,12])
print('\n-------------------------------')
print('无序单链去重操作接口测试：deduplitcate,\n单链去重操作接口测试： ')
print('测试链表：',end=' ')
myList3.printList()
delCount = myList3.deduplitcate(sorted=False)
print('去重共 删除了{}个结点'.format(delCount))
print('去重得到的链表为：',end=' ')
myList3.printList()

#有序去重测试
myList4 = LinkList()
myList4.init_fromList([1,1,2,2,2,3,3,3,3,9,9,9,10])
print('\n-------------------------------')
print('无序单链去重操作接口测试：deduplitcate,\n单链去重操作接口测试： ')
print('测试链表：',end=' ')
myList4.printList()
delCount = myList4.deduplitcate(sorted=True)
print('去重共 删除了{}个结点'.format(delCount))
print('去重得到的链表为：',end=' ')
myList4.printList()