class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        acc = 0

        for i in nums:
            if acc < 0:
                acc = i
            else:
                acc += i
            
            best = max(best, acc)
        return best
                
        