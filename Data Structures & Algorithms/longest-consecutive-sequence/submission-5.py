class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        d = set(nums)
        longest = 1
        for num in d:
            if num - 1 in d:
                continue
            i = 1
            while True:
                if num + i in d:
                    i += 1
                else:
                    break
            longest = max(longest, i)
        return longest