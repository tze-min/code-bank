class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # method 1: linear search, O(n) time  

        for i in range(len(nums)):
            if target <= nums[0]: # first
                return 0
            elif target == nums[-1]: # equals last
                return len(nums) - 1
            elif target > nums[-1]: # more than last
                return len(nums)
            elif target == nums[i]:
                return i
            elif target > nums[i] and target < nums[i+1]:
                return i + 1

        # method 2: binary search, O(logn) time
        