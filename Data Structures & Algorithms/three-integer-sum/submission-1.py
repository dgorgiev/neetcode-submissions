class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            # -nums[i] == nums[j] + nums[k]
            target = -nums[i]
            def twoSum(j: int, k: int, target: int):
                while j < k:
                    left = nums[j]
                    right = nums[k]
                    s = left + right
                    if s == target:
                        res.append([-target, left, right])
                        while j < k and nums[j] == left and nums[k] == right:
                            j += 1
                            k -= 1
                    elif s < target:
                        j += 1
                    else:
                        k -=1
            twoSum(i+1, n-1, target)
        return res
                    