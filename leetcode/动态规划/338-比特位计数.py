#338-比特位计数

'''
给定一个非负整数 num。
对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

输入: 5
输出: [0,1,1,2,1,2]
'''

'''
解法一：
1.偶数的二进制最右边为0，那么将这个偶数右移一位的二进制中1的个数不变，
	因此偶数的二进制中1的个数为右移一位的二进制数中1的个数
2.奇数的二进制最右边为1，那么将这个奇数右移一位的二进制中1的个数减一，
	因此奇数的二进制中1的个数为右移一位的二进制数中1的个数再加上1
'''
class Solution1(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num<0:
            return 0
        if num==0:
            return [0]
        if num==1:
            return [0,1]
        res = [None]*(num+1)
        res[0],res[1]=0,1
        for i in range(2,num+1):
            res[i]=res[i>>1] if i%2==0 else res[i>>1]+1
        return res
        

'''
解法二：
考虑n&(n-1)的意义：
1.一个数n，减去1，相当于在其二进制的右边借1，直到找到一位为1，那么这位变为0，右边的各个位置变为1
比如说n=8，二进制为xxxx1000，n-1=7，二进制为xxxx0111
2.如果我们将n&(n-1)，得到的二进制就变为xxxx0000，显然，原来的二进制数的最右边的1变为0

对于本题来说，n的二进制中1的个数就是n&(n-1)二进制数中1的个数加1
'''
class Solution2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num<0:
            return 0
        res = [0]
        if num==0:
            return res
        for i in range(1,num+1):
            res.append(res[i&(i-1)]+1)
        return res
        