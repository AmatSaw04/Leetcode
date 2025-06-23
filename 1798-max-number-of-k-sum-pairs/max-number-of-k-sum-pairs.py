class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        i = 0
        a = 0
        j = len(nums) -1
        while i < j:
            cur_sum = nums[i]+nums[j] 
            if cur_sum == k:
                a+=1
                i+=1
                j-=1
            elif cur_sum < k:
                i+=1
            else:
                j-=1
        return a


        