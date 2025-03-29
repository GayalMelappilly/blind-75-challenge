class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]*len(nums)
        leng = len(nums)

        product = 1
        for i in range(leng):
            result[i] = product
            product *= nums[i]  

        product = 1
        for i in range(leng-1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result
        
           
            
                             

            