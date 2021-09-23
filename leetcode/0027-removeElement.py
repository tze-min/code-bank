class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        index = 0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1
        return index