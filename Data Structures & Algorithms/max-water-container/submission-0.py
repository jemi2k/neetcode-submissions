class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_amount = 0

        left = 0
        right = len(heights) - 1

        while left < right:

            if heights[left] < heights[right]:
                height = heights[left]
            
            else: 
                height = heights[right]

            
            curr_amount = height * (right - left)

            max_amount = max(max_amount, curr_amount)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            

        
        return max_amount
            




        