class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        a = nums[-k]
        return a
        