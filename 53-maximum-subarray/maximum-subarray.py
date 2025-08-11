class Solution(object):
    def maxSubArray(self, nums):
        a = float('-inf')
        b = 0
        for num in nums:
            b += num
            if b > a:
                a = b
            if b < 0:
                b =0
        return a


        