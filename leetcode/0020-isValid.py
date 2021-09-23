class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}
        
        for b in s:
            if b in "([{":
                stack.append(b)
            elif len(stack) == 0:
                return False
            elif brackets[b] == stack[-1]:
                stack.pop()
            else:
                return False
    
        return True if len(stack) == 0 else False