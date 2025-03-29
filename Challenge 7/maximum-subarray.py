class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currSum = 0

        for i in nums:

            currSum += i
            if i>currSum:
                currSum = i
            if currSum > maxSum:
                maxSum = currSum

        return maxSum    