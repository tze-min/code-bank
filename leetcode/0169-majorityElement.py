class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # method 1: Boyer-Moore algo, O(n) time and O(1) space

        majority, count = nums[0], 0 # assume the 1st number is the majority element + this is O(1) space

        for n in nums: # O(n) time
            if n == majority:
                count += 1
            elif count == 0: # since this problem assumes a majority element exists, if a numbers count == 0 we can be sure it's not majority
                majority, count = num, 1 # and so we reset the majority element
            else:
                count -= 1

        return majority

        # method 2: dictionary

        d = dict() # O(n) space
        for n in nums: # O(n) time
            d[n] = d.get(n, 0) + 1 # note use of d[n] vs d.get(n, 0)
            if d[n] > len(nums) // 2:
                return n