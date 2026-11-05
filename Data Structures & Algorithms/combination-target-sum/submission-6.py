class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sols = []
        def rec(i: int, sol: List[int], acc: int):
            remaining = target - acc
            val = nums[i]
            if remaining == 0:
                sols.append(sol.copy())
                return
            if val <= remaining:
                s = sol.copy()
                s.append(val)
                rec(i, s, acc+val)
            if i < len(nums) - 1:
                rec(i+1, sol.copy(), acc)
            

        rec(0, [], 0)
        return sols