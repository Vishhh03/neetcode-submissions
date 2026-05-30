class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums [i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                while total > 0 and left < right:
                    right -= 1
                while total < 0 and left < right:
                    left += 1
        return output