class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Going from reverse to find the optimal path
        goal = len(nums) -  1

        #1-2-0-1-0    
        # can goal-1 reach goal? if yes we only have to reach goal-1 index, new goal gets updated, else continue backwards
        for i in range(goal-1, -1, -1):
            if nums[i] >= goal - i:
                goal = i

        return True if goal == 0 else False