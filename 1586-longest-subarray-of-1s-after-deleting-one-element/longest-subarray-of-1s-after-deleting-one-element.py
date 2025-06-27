class Solution(object):
    def longestSubarray(self, nums):
        a = 0
        max_one = 0
        left = 0
        right = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                a+=1
            while a > 1:
                if nums[left] == 0:
                    a -=1
                left+=1
            max_one = max(max_one, right - left)
        return max_one
