class Solution:
    def findMin(self, nums: List[int]) -> int:
        li = 0
        ri = len(nums) - 1
        mi = li + (ri-li) // 2

        while li < ri:
            l = nums[li]
            r = nums[ri]
            m = nums[mi]

            if l <= m and m < r:
                return l
            if l <= m and m > r:
                if ri == mi+1:
                    return r
                li = mi
                mi = li + (ri-li) // 2
                continue
            if l > m and m < r:
                if li == mi-1:
                    return m
                ri = mi
                mi = li + (ri-li) // 2
                continue
            if l > m and m > r:
                return r
        return nums[mi]

        
            

