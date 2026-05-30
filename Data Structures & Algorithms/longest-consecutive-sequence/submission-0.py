class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maximum = 0
        for num in nums:
            count = 1
            if num-1 not in numsSet:    #START OF SEQUENCE
                i = 1
                while num+i in numsSet:
                    count += 1
                    i += 1
                maximum = max(count, maximum)
            #if num+1 not in numsSet:    #END OF SEQUENCE

        return maximum