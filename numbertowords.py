class Solution:
    def numberToWords(self,num):
## this code is based on Stefan's awesome solution (https://leetcode.com/stefanpochmann/)
        """
        :type num: int
        :rtype: str
        """
        lessthan20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:
                return lessthan20[n-1:n]
            if n < 100:
                return [tens[int(n/10)-2]] + words(n%10)
            if n < 1000:
                return [lessthan20[int(n/100)-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million','Billion'),1):
                if n < 1000**(p+1):
                    return words(int(n/1000**p)) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'
