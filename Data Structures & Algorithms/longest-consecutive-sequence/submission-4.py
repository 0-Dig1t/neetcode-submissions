class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class DSU():
            def __init__(self, nums):
                self.parents = {i: i for i in nums}
                self.ranks = {i: 1 for i in nums}
                self.res = 1 if nums else 0

            def find(self, x):
                # if we reach the root then we return root
                if self.parents[x] == x:
                    return x
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

            def union(self, u, v):
                # find the roots of the nodes
                i = self.find(u)
                j = self.find(v)

                # if they equal then just return
                if i == j:
                    return

                if self.ranks[i] > self.ranks[j]:
                    self.parents[j] = i
                    self.ranks[i] += self.ranks[j]
                elif self.ranks[i] < self.ranks[j]:
                    self.parents[i] = j
                    self.ranks[j] += self.ranks[i]
                else:
                    self.parents[j] = i
                    self.ranks[i] += self.ranks[j]
                
                self.res = max(self.res, self.ranks[i], self.ranks[j])

        dsu = DSU(nums)
        numSet = set(nums)
        for num in nums:
            if num + 1 in numSet:
                dsu.union(num, num + 1)
        
        return dsu.res
        
