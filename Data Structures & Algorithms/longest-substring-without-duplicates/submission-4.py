class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best, curr = 0, 0
        n = len(s)

        l, r = 0, 0
        while r <= n - 1:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                curr += 1
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
                r += 1
                best = max(best, curr)
                curr = r - l

        best = max(best, curr)

        return best


        