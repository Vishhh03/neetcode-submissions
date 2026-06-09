class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            if target == nums[mid]:
                    return mid
            #Check if target present between the sorted side
            if nums[mid] <= nums[right]:    #If right is greater that mid, right part is sorted 
                if nums[mid] < target <= nums[right]: #If target in right side
                    left = mid+1
                else:                                #If target in left side
                    right = mid
            else: #Left side is sorted, right side is unsorted
                if nums[left] <= target < nums[mid]:
                    right = mid+1
                else:
                    left = mid
        return -1