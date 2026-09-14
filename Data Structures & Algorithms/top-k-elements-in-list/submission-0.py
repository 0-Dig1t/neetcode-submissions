class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        sortFreq = sorted(freq, key=freq.get, reverse=True)
        for i in range(k):
            res.append(sortFreq[i])
        return res