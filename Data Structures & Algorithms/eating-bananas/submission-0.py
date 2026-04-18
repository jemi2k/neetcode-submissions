from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def k_iswork(k):
            hour = 0
            for p in piles:
                hour += ceil(p/k)
            return hour <= h

        

        left = 1
        right = max(piles)

        while left < right:
            k = (left+right) // 2

            if k_iswork(k):
                right = k
            else:
                left = k + 1
        return right
            





        
