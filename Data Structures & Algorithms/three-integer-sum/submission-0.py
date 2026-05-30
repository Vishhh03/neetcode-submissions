class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    right += 1
                    left += 1
                    break
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    left += 1
        return output