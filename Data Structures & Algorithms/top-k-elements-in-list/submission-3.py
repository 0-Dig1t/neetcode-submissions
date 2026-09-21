from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for element, idx in freq.items():
            buckets[idx].append(element)
        
        count = 0
        for i in range(len(buckets)-1, -1, -1):
            if count >= k:
                break
            for element in buckets[i]:
                if count >= k:
                    break
                res.append(element)
                count += 1

        return res