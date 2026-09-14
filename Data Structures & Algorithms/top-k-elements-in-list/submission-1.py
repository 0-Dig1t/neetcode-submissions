from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = defaultdict(int)
        heap = []
        
        for num in nums:
            count[num] += 1
        
        for key, val in count.items():
            heapq.heappush(heap, (-val,key))

        for i in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)

        return res