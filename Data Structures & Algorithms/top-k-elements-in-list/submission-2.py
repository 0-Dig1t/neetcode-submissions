from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] += 1
        
        for key, val in count.items():
            buckets[val].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            bucket = buckets[i]
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res
                
        return res