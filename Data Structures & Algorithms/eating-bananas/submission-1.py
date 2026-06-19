from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hoursToEat(speed):
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i]/speed)
            return hours
                
        # min_hours = float('inf')
        
        # for speed in range(1,max(piles)+1):
        #     hours = hoursToEat(speed)
        #     if hours <= h:
        #         return speed 


        left = 1
        right = max(piles)

        while left<=right:
            mid = (left+right)//2

            if hoursToEat(mid) > h:
                left = mid+1
            else:
                right = mid-1

        return left