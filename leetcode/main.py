#找零
def minChange(N):
	m = 1024-N

	numOf64 = m%64
	m = m//64

	numOf16 = m%16
	m = m//16

	numOf4 = m%4
	m = m//4

	numOf1 = m

	return numOf64+numOf16+numOf4+numOf1

#2.
import sys
def dealLine(line):
    index = 0
    while index<len(line):
        case1 = line[index:index+3]
        if len(case1) == 3 and case1[0] == case1[1] == case1[2]:
            del line[index]
            continue
        case2 = line[index:index+4]
        if len(case2) == 4 and case2[0] == case2[1] and case2[2] == case2[3]:
            del line[index+3]
            continue
        index+=1
    return ''.join(line)

if __name__ == "__main__":
    N = int(input())
    for test in range(N):
        line = sys.stdin.readline()
        print (dealLine(list(line)[0:-1]))



#3.奖品分配
def rotate(res,m,A):
	#m:人数
	#A：得分值
	#res:list 分别对应对应位置的最小奖品数
	start = argmin(A)
	res[start]=0
	#1.顺时针开始
	i = start
	while A[i%m]<A[(i+1)%m]:
		res[(i+1)%m] = res[i%m]+1
		i+=1
	#2.逆时针
	j = start
	while A[j%m]<A[(j-1)%m]:
		res[(j-1)%m] = res[j%m]+1
		j+=1

	return res,i,j

def queue(res,m,start,end,A):
	if start==end:
		res[start]=1
		return
	index = argmin(A[start,end+1])
	