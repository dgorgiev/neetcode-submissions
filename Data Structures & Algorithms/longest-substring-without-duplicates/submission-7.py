class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        n = len(s)

        l, r = 0, 0
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
                r += 1

            best = max(best, r - l)

        return best


        