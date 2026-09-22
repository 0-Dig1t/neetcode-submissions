class UnionFind:
    def __init__(self, nums):
        self.parents = {x: x for x in nums}
        self.ranks = {x: 1 for x in nums}

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if self.ranks[parent_x] < self.ranks[parent_y]:
            self.parents[parent_x] = parent_y
            self.ranks[parent_y] += self.ranks[parent_x]
        else:
            self.parents[parent_y] = parent_x
            self.ranks[parent_x] += self.ranks[parent_y]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        uf = UnionFind(nums)
        for num in num_set:
            if num + 1 in num_set:
                uf.union(num, num+1)

        return max(uf.ranks.values()) if uf.ranks else 0