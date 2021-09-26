class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # method 1, recursion: runtime 57 ms
        def helper(digits):
            if len(digits) == 0:
                return [1]
            elif digits[-1] < 9:
                digits[-1] += 1
                return digits
            digits[-1] = 0
            return helper(digits[:len(digits)-1]) + digits[len(digits)-1:]
        
        return helper(digits)

        # method 2, consider the quicker way of str -> int + 1 -> str: runtime 37ms
        str_digits = "".join(str(i) for i in digits)
        int_digits = int(str_digits) + 1
        str_digits = str(int_digits)
        return list(str_digits) # not quicker than defining result = [] and appending ints to it