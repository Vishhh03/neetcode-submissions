class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # each index lets check what is the subarray of largest sum till that point
        # for 2, it will be 2, for -3 it will be either just -3 or sum of -3+2=-1 since -1 is larger we continue
        # for 4, it will be either just 4 or 4+-1=3, since 4 is larger we ignore 2 and -3 from subarryas going forward
        # each iteration we keep storing the result in a result output variable by taking max
        result = nums[0]
        curr = nums[0]
        if len(nums)>1:
            left = 0
            for right in range(1,len(nums)):
                num = nums[right]
                curr = max(num, num+curr)
                result = max(curr, result)
                if curr == num:
                    left += 1
                else:
                    continue
        return result