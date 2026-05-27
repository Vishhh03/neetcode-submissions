class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            left_h = heights[left]
            right_h = heights[right]
            if left_h > right_h:
                area = right_h * (right - left)
                res = max(area, res)
                right -= 1
            else:
                area = left_h * (right - left) 
                res = max(area, res)        
                left += 1

        return res