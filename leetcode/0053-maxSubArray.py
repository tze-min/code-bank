class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # Kadane's algorithm
        
        curr_sum, max_sum = 0, -10**4
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum