class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        def returnIndex(l, r, m):
            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            elif target == nums[m]:
                return m
            else:
                return None
    
        while l <= r:
            m = (l+r) // 2
            res = returnIndex(l, r, m)
            if res is not None:
                return res
            elif target >= nums[m]:
                l = m+1
            else:
                r = m-1
        return -1
            