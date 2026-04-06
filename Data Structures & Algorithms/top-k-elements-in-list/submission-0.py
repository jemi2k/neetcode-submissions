from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = [[] for _ in range(len(nums)+1)]
        result = []

        for num, f in freq.items():
            res[f].append(num)
        
        for i in range(len(res)-1, 0, -1):
            for j in res[i]:
                result.append(j)
                if len(result) == k:
                    return result




        