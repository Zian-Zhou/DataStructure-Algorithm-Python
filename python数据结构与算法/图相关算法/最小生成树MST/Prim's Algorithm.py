#最小生成树MST
#Minimal spanning tree

'''
设G=（V,E）是一个无向连通图，生成树各边的权值之和称为该生成树的代价。在G的所有生成树中，代价最小的生成树称为最小生成树。

实际应用例如，字啊n个城市之间建造通信网络，至少要架设n-1条通信线路，没两个城市之间架设的成本不一样，求最经济的方案。
'''


'''
https://www.cnblogs.com/nannanITeye/p/3446424.html

Prim算法的基本思想：

设G=(V,E)是一个无向连通图，，令T=(U,TE)是G的最小生成树。T的初始状态为U={v0},TE={}.重复下述操作：
在U的所有节点，以及V-U钟的所有节点中，找到代价最小的边(u,v)加入到集合TE，同时将v并入U，直到U=V为止。

因此关键就在于怎么找到这样的代价最小的边。我们可以用两个数组来存储候选最短边的相关信息：
	lowcost：表示所有顶点到当前生成树T的最短距离，如果顶点已经在生成树中，那么对应距离为0，表示已经访问过；
	adjvex：表示lowcost中对应的边的邻接点，当我们找到最短边的时候，就可以对应找到边的起点，也就可以表示出来一条边了；
			注意，这个边的起点指的是对应的在T中的那一端，而另外一个端点是我们遍历过程中的点，因此算法中我们只要遍历不在
			当前生成树的点集，就可以找到一条最短边（u，v），这就符合MST性质了。

接下来算法实现就非常简单。我们先选择一个起点作为算法的开始（默认为v0），然后初始化lowcost以及adjvex。接下来循环n-1次，找到
对应的n-1条边，则可以表示出我们的最小生成树。
每一次循环中，我们都遍历所有点，找到lowcost中最小的非零值（非零保证了遍历的这个点不是生成树中的点，也即还未访问的点），也就
找到一个下一个要加入T的端点，同时我们在adjvex中找到这条边对应在T中的另一个端点，从而我们就可以表示出这一条边了。
遍历完毕之后我们就得到MST了。

算法时间复杂度只与顶点个数有关，为O(n^2)，n为顶点数。因此Prim算法适合稠密图，就是边比较多，相比之下顶点数目比较小的；
缺点就是当边比较稀少的时候时间不是最优的，同时由于要维护顶点矩阵，因此当顶点特别多的时候时间和空间的开销都不可接受。

'''


def Prim(startPoint=0, graph):
	'''
	graph:图(arc-带权边，二维数组；vertexNum-图的顶点数量)
	startPoint：指定起点编号，默认为0
	'''
	sumCost = 0
	#1.初始化两个数组
	lowcost = [0 for _ in range(graph.vertexNum)]
	adjvex = [None for _ in range(graph.vertexNum)]
	for i in range(graph.vertexNum):
		lowcost[i] = graph.arc[startPoint][i]
		adjvex[i] = startPoint

	#lowcost[startPoint]=0#将顶点stratPoint加入集合U，实际上这一步在上面循环中已经执行了，这里只是提醒一下0的具体意义
	
	#2.开始n-1次循环找到n-1条边
	for i in range(1,graph.vertexNum):
		#2.1遍历lowcost找最小代价边
		minCost = float('inf')
		for j in range(graph.vertexNum):
			if lowcost[j]!=0 and lowcost[j]<minCost:#非零表示还未访问过
				minCost = lowcost[j]#最短边的权值
				currPoint = j#对应找到最短边的一个端点

		#2.2输出最短边
		print("({0},{1}):{2}".format(adjvex[currPoint],currPoint,minCost))#(i,j):weight,i为集合U中点，j为待加入的点
		sumCost+=minCost

		#2.3将顶点currPoint加入集合U
		lowcost[currPoint]=0

		#2.4根据新加入的点，更新两个数组
		for j in range(graph.vertexNum):
			if j!=currPoint and graph.arc[currPoint][j]<lowcost[j]:
				'''
				j!=currPoint:不需要对当前点进行更新，前面一步已经更新过了
				graph.arc[currPoint][j]<lowcost[j]：由于U中新加入顶点，所以在集合U和V-U之间，可能存在更短的边，因此需要更新
				'''
				lowcost[j] = graph.arc[currPoint][j]
				adjvex[j] = currPoint





#==================================测试用例==================================
if __name__ == '__main__':
	class graph():
	    def __init__(self):
	        self.arc = [[]]
	        self.vertexNum = 0
	        
	    def matrix2graph(self,matrix):
	        self.vertexNum = len(matrix)
	        self.arc = matrix

	maxInt = float('inf')
	matrix = [[0,34,46,maxInt,maxInt,19],
	          [34,0,maxInt,maxInt,12,maxInt],
	          [46,maxInt,0,17,maxInt,25],
	          [maxInt,maxInt,17,0,38,25],
	          [maxInt,12,maxInt,38,0,26],
	          [19,maxInt,25,25,26,0]
	         ]

	G = graph()
	G.matrix2graph(matrix)

	Prim(G,0)
	'''
	(0,5):19
	(5,2):25
	(2,3):17
	(5,4):26
	(4,1):12
	'''