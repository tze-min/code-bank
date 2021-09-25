class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
        
        
"""
Test cases:
"aaa"
"aaaa"
ans: -1

"a"
"a"
ans: 0

"mississipi"
"issip"
ans: 4

"mississipi"
"issipi"
ans: -1

"mississipi"
"sippia"
ans: -1

"abc"
"c"
ans: 2
"""