class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while True:
            mid = (left+right) //2
            if nums[(mid)] > nums[right]:
            #If middle is greater than left end, left side is ordered wrong. 
                #Check if middle is inflection, else find new center in left.
                if nums[mid] > nums[(mid)+1]:
                    return nums[mid+1]
                else:
                    left = mid
            else:
                right = mid
