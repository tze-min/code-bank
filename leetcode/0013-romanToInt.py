class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        
        d = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        for i in range(len(s)-1):
            curr = d[s[i]]
            # keep adding each letter unless its value < next letter's value
            
            if curr < d[s[i+1]]:
                res -= curr
            else:
                res += curr
                
        return res + d[s[-1]]