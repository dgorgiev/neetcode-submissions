class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        i = n // 2
        while True:
            nb = nums[i]
            if nb == target:
                return i

            if left >= i-1 and right <= i+1:
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                return -1
            if nb < target:
                left = i
                i = (right + i) // 2
                continue
            if nb > target:
                right = i
                i = (left + i) // 2
                continue
        
        return -1