class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
                
        shortest_word = min(strs, key = len)
       
        for i, val in enumerate(shortest_word):
            for word in strs:
                if word[i] != val:
                    return shortest_word[:i]
        
        return shortest_word