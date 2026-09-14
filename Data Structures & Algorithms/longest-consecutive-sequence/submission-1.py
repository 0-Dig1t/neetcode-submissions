class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = set(nums)
        # parents = [i for i in range(len(nums))]
        # ranks = [0] * len(nums)

        # def find(x):
        #     # if we reach the root then we return root
        #     if parents[x] == x:
        #         return x
        #     parents[x] = find(parent[x])
        #     return parents[x]

        # def union(u, v):
        #     # find the roots of the nodes
        #     i = find(u)
        #     j = find(v)

        #     # if they equal then just return
        #     if i == j:
        #         return

        #     if ranks[i] > ranks[j]:
        #         parents[j] = i
        #     elif ranks[i] < ranks[j]:
        #         parents[i] = j
        #     else:
        #         parents[j] = i
        #         ranks[i] += 1

        res = 0
        table = set(nums)
        for i in range(len(nums)):
            curr = nums[i]
            if curr - 1 not in table:
                length = 1
                while curr + 1 in table:
                    length += 1
                    curr += 1
                res = max(length, res)

        return res
        
