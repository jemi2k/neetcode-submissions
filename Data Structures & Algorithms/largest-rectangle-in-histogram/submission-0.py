class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:

                h, j = stack.pop()
                a = (i-j) * h
                max_area = max(max_area, a)
                start = j
            stack.append((height,start))

        while stack:
            h, j = stack.pop()
            a = (n-j) * h
            max_area = max(max_area, a)
        
        return max_area

        


                
        