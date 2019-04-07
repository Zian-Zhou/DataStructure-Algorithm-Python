#6. Z字形变换

'''(其实是N字形)
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''

#解法一
'''
	nrows=1:
		0 1 2 3 4 5 6 ...

	nrows=2:
		0 2 4 6 ...
		1 3 5 7 ...

	nrows=3:
		0   4   8     12
		1 3 5 7 9  11 ...
		2   6   10    ...

	nrows=4:
		0      6        12
		1    5 7     11 13
  		2  4   8  10    14
		3      9		...

	观察规律可以发现，除了nrows=1的情况之外，其他的情况下，都有下列规律：
		第0行：       下标相隔2*(nRows-1),对应的下标则为k*cycleLen   cycleLen = 2*(nRows-1)
		第nrows-1行： 下标相隔2*(nRows-1),对应的下标则为k*(cycleLen)+nrows-1
		第i行：       下标除了有k*(cycleLen)+i之外，还有(k+1)*(cycleLen)-i
	根据以上规律就可以设计算法实现了。
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or not numRows or numRows==0:
        	return ''
        if numRows==1:
        	return s
        ret = ''
        cycleLen = 2*(numRows-1)
        for i in range(numRows):
        	j = 0
        	while j+i<n:#j+i<n确保下标在字符串长度以内
        		ret+=s[j+i]
        		if i!=0 and i!=numRows-1 and j+cycleLen-i<n:#j+cycleLen-i<n确保下标在字符串长度以内
        			ret+=s[j+cycleLen-i]
        		j+=cycleLen
        return ret