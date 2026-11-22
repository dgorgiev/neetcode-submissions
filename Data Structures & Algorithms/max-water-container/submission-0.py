class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maximize height and width
        n = len(heights)

        best = min(heights[0], heights[n-1]) * (n-1)

        l = 0
        r = n-1
        while l < r:
            best = max(best, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return best
        