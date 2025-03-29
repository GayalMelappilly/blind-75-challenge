class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:      
            
        leng = len(nums)
        res = []

        nums.sort()
        
        if nums[leng-1] < 0 or nums[0] > 0:
            return []
        elif nums[leng-1] == 0 and nums[0] == 0:
            return [[0,0,0]]

        for i in range(leng):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            low = i+1
            high = leng-1

            while low < high:
                while low>i+1 and nums[low-1] == nums[low] and low<high:
                    low += 1
                if low>=high:
                    break
                arr_sum = nums[i]+nums[low]+nums[high]
                if arr_sum<0:
                    low += 1
                elif arr_sum>0:
                    high -= 1
                else:
                    res.append([nums[i],nums[low],nums[high]])
                    low += 1
                    high -= 1
        return res