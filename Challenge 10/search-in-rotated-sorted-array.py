class Solution:
    def search(self, nums: List[int], target: int) -> int:

        leng = len(nums)
        l, r = 0, leng-1

        if nums[0] == target:
            return 0

        for i in range(leng-1):
            if nums[i]>nums[i+1] and i<leng-1:
                if target>nums[l]:
                    r = i
                else:
                    l = i

        mid = (l+r)//2       

        while l<r:
            if target == nums[mid]:
                return mid
            if target == nums[mid+1]:
                return mid+1  
            if r-l == 1 and target != nums[mid] and target != nums[mid+1]:
                return -1  
            if target<nums[mid]:
                r = mid
            elif target>nums[mid]:
                l = mid   
            mid = (l+r)//2           
        return -1  