class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        return (res if x >= 0 else -res) if res.bit_length() < 32 else 0