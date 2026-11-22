class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            res.append(nums[i-1] * res[i-1])
            
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            res[i] = res[i] * nums[i + 1] * prod
            prod *= nums[i + 1]

        return res