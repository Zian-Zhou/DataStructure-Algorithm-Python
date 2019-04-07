#3. 无重复字符的最长子串

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s)<=1:
        	return len(s)
        str_index = {}
        start = 0#记录重复数字位置+1
        max_len = 0
        for i in range(len(s)):#遍历所有位置的字符
        	if s[i] in str_index and str_index[s[i]]>=start:
        	#如果当前字符曾经出现过，并且先前出现的位置在start及其之后的位置
        		start = str_index[s[i]]+1#调整以当前字符结尾的最长不重复子串的开头
    		str_index[s[i]] = i#更新当前字符在字典中的下标
        	max_len = max(i-start+1, max_len)#更新最长长度
        return max_len

'''
以s = 'abcabc'为例：

当i遍历到3，即s[i]=a时，a是已经出现过的字符，并且字典中a的下标是0，刚好就是start：
	因此，start右移一位，变为1，并且计算当前最长长度，3-1+1=3
直到最后一个字符遍历完毕，返回最长长度3
'''