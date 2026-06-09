class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right) //2
            if nums[mid] > nums[right]:
            #If middle is greater than left end, left side is ordered wrong. 
                left = mid+1
            else:
                right = mid
        return nums[left]