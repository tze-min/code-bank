class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum("+" in s or -1 for s in operations)

        """
        x = 0
        for s in operations:
            if s[0] == "+" or s[2] == "+":
                x += 1
            elif s[0] == "-" or s[2] == "-":
                x -= 1
        return x
        """