class Solution:
    def productExceptSelf(self,nums):
        result = []
        n = len(nums)
        value = 1
        for i in range(0,n):
            result.append(value)
            value = value * nums[i]

        value = 1
        for i in range(n-1,-1,-1):
            result[i] = result[i] * value
            value = value * nums[i]

        return result
