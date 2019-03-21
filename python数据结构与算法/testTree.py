#根据先序遍历序列和中序遍历序列构建二叉树，并输出

from BinTree import BinTree

newTree = BinTree()
newTree.reConstructBinTree(preOrderList = [1,2,4,7,3,5,6,8], inOrderList = [4,7,2,1,5,3,8,6])

print('=======================================')
print('tree list : \n',newTree.print_tree_list())

print('=======================================')
print('preOrder list : ')
newTree.preOrder()

print('=======================================')
print('inOrder list : ')
newTree.inOrder()

print('=======================================')
print('postOrder list : ')
newTree.postOrder()

print('=======================================')
print('levelOrder list : ')
newTree.levelOrder()













