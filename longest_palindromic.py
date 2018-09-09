class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        while length >=1:
            for i in range(0,len(s)-length+1):
                print(i)
                if s[i:length+i] == s[i:length+i][::-1]:
                    return s[i:length+i]
            length =length - 1
            print(length)
        return ""
