class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums) < k:
            return 0
        current_sum = sum(nums[0:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            if current_sum > max_sum:
                max_sum = current_sum
        return float(max_sum) / k