class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = dict()
        for i, num in enumerate(nums):
            if target - num in prev_map:
                return [i, prev_map[target-num]]
            prev_map[num] = i    
        return -1
        