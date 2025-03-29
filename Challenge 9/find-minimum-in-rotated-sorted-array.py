class Solution:
    def findMin(self, nums: List[int]) -> int:

        leng = len(nums)
        mid = leng//2
        l = 0
        r = leng-1

        if leng == 1:
            return nums[0]
        if not nums:
            return nums    
        
        while l<r:
            if r-l == 1:
                if nums[r]>nums[l]:
                    return nums[l]
                else:
                    return nums[r] 
            if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            if nums[mid]>nums[l] and nums[mid]>nums[r]:
                if nums[l]>nums[r]:
                    l = mid
                else:
                    r = mid
            elif nums[mid]<nums[l] and nums[mid]<nums[r]:
                if nums[l]>nums[r]:
                    r = mid
                else:
                    l = mid
            else:
                return nums[0] 
            mid = (l+r)//2    
