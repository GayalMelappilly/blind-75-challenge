class Solution:
    def maxArea(self, height: List[int]) -> int:

        leng = len(height)-1
        left, right = 0, leng
        container = 0
  
        while left < leng:

            short = height[right] if height[left]>height[right] else height[left]

            length = right - left
            area = length * short

            if area > container:
                container = area

            if short == height[right] and right != 0:
                right -= 1
            else:
                left += 1 

            if right <= (leng//2) and left >= (leng//2):
                return container      

        return container        





      
            
            
        