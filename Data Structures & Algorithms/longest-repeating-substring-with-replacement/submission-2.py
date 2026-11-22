class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        maxf = 0
        best = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])

            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1) 

        return best


        