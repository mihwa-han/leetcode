##Reverse Words in a String II
'''
  Given an input string , reverse the string word by word. 

  Example:

  Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
  Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
  Note: 

  A word is defined as a sequence of non-space characters.
  The input string does not contain leading or trailing spaces.
  The words are always separated by a single space.
  Follow up: Could you do it in-place without allocating extra space?
'''

class Solution:
    def reverseWords(self, str):
        reverse = str[::-1]
        temp = ''.join(reverse)
        a=[]
        for i,n in enumerate(temp.split()):
            if i==0:
                a+=n[::-1]
            else:
                a.append(' ')
                a+=n[::-1]
        return a
