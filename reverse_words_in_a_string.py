class Solution:
    def reverseWords(self, s):
        s=s[::-1]
        beg = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s[beg:i] = s[beg:i][::-1]
                beg = i + 1
            elif i == len(s) -1:
                s[beg:i+1] = s[beg:i+1][::-1]
        return(s)
