class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res= [1] * length
        pre = 1
        for i in range(1,length):
            res[i] = nums[i-1] * pre
            pre = res[i]
        print(res)
        
        pre = 1
        for j in range(length-2,-1,-1):     
            res[j] = res[j]*(nums[j+1] * pre) 
            pre = nums[j+1] * pre           
                                
        print (res)

        return res