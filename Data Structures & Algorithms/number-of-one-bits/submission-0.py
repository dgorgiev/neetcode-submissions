class Solution:
    def hammingWeight(self, n: int) -> int:
        acc = 0
        while n > 0:
            if n%2 == 1:
                acc += 1
            n = n >> 1
        return acc
        