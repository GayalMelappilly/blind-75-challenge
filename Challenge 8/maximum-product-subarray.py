class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        max_product = 0
        product = 1
        after_neg = 1
        neg_found = False


        for num in nums:
            if num == 0:
                if product>max_product and product>1:
                    max_product = product
                if after_neg>max_product and after_neg>1:
                    max_product = after_neg
                after_neg = 1
                neg_found = False
                product = 1
                continue
            if neg_found is True:
                after_neg *= num
            product *= num
            if product>max_product:
                max_product = product
            if num>max_product:
                max_product = num 
            if num < 0:
                neg_found = True

        if neg_found is True and after_neg>max_product and after_neg>1:   
            return after_neg
        else:
            return max_product           

                

        
        