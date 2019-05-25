'''
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
'''

#解答：
'''
采用类似滑动窗口的思路，即用两个指针表示窗口左端left和右端right。
向右移动right，保证left与right之间的字符串足够包含需要包含的所有字符，
而在保证字符串能够包含所有需要的字符条件下，向右移动left，保证left的位置对应为需要的字符，这样的
窗口才有可能最短，此时只需要判断当期窗口的长度是不是目前来说最短的，决定要不要更新minL和minR（这两个
变量用于记录可能的最短窗口的端点）

搞清楚指针移动的规则之后，我们需要解决几个问题，就是怎么确定当前窗口包含所有需要的字符，以及怎么确定left的
位置对应的是需要的字符。
这里我们用一个字典mem保存目标字符串t中所含字符及其对应的频数。比如t="ABAc",那么字典mem={"A":2,"B":1,"c":1},
只要我们在向右移动right的时候，碰到t中的一个字符，对应字典的计数就减一，那么当字典这些元素的值都不大于0的时候，
我们的窗口里面就包含了所有需要的字符；但判断字典这些元素的值都不大于0并不能在O(1)时间内实现，因此我们要用一个变量
来记录我们遍历过字符数目，记为t_len，当我们遍历s的时候，碰到字典中存在的字符且对应频数大于0，就说明我们还没有找到
足够的字符，那么就要继续向右移动right，此时t_len-=1；直到t_len变为0，就说明此时已经找到足够的字符保证窗口符合要求了。

所以接下来就是移动left。我们需要移动left，直到找到目标字符串中的字符，同时又希望窗口尽可能短，因此我们就希望找到的
left使得窗口的开头就是要求的字符串中的字符，同时整个窗口含有所有需要的字符数量。注意到，前面我们更新字典的时候，
比如字符"A",如果我们窗口里面有10个A，而目标字符串中有5个A，那此时字典中A对应的计数就是-5，那么我要收缩窗口又要保证
窗口能够包含所需的字符，那么我们就要在收缩窗口的时候增加对应字符在字典的计数，直到我们找到某个位置的字符A，此时字典中
的计数为0，就不可以再收缩了（如果此时继续移动left，那么之后的窗口就不可能含有A这个字符了），此时窗口为可能的最小窗口，比较
更新记录即可。


'''
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mem = defaultdict(int)
        for char in t:
        	mem[char]+=1
        t_len = len(t)

        minLeft, minRight = 0,len(s)
        left = 0

        for right,char in enumerate(s):
        	if mem[char]>0:
        		t_len-=1
        	mem[char]-=1

        	if t_len==0:
        		while mem[s[left]]<0:
        			mem[s[left]]+=1
        			left+=1

        		if right-left<minRight-minLeft:
        			minLeft,minRight = left,right

        		mem[s[left]]+=1
        		t_len+=1
        		left+=1
        return '' if minRight==len(s) else s[minLeft:minRight+1]
