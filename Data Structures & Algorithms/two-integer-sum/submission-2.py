class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        n = len(nums)
        for i in range(n):
            if nums[i] in d:
                j = d[nums[i]]
                if j != i:
                    return [i, j] if i < j else [j, i]
            else:
                d[target - nums[i]] = i
