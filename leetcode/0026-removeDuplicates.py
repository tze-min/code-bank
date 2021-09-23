class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        curr = nums[0]
        index = 1
        for i in nums[1:]:
            if i > curr:
                curr = i
                nums[index] = curr
                index += 1
                
        return index