class Solution(object):
    def longestOnes(self, nums, k):
        i = 0
        j = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k-=1
            if k < 0:
                if nums[i] == 0:
                    k+=1
                i+=1
        return j - i+1





        