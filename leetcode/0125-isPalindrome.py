class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]", "", s.lower())
        leng = len(s)
        even = leng % 2 == 0 and s[:leng//2][::-1] == s[leng//2:]
        odd = leng % 2 != 0 and s[:leng//2][::-1] == s[1 + leng//2:]
        return True if even or odd else False