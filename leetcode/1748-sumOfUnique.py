class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        # method 1, loop count and add (slower)
        res = 0
        for i in nums:
            if nums.count(i) == 1:
                res += i
        return res

        # method 2, list comprehension (quicker)
        unique = []
        [unique.append(i) for i in nums if nums.count(i) == 1]
        return sum(unique)