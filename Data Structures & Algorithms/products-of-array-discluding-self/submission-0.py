class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prod = 1
        for i in range(len(nums)):
            prefix.append(prod)
            prod *= nums[i]
            
        suffix = [1 for _ in range(len(nums))]
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = prod
            prod *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res