##  First Unique Character in a String
'''
Given a string, find the first non-repeating character in it 
and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

class Solution:
    def firstUniqChar(self, s):
        d={}
        for i in list(s):
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for n,i in enumerate(list(s)):
            if d[i]==1:
                return n
        return -1
