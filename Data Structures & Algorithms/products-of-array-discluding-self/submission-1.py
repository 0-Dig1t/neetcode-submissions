class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = [nums[0]] * len(nums)
        suffix = [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]

        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[i+1])
            elif i == len(nums)-1:
                res.append(prefix[i-1])
            else:                
                res.append(prefix[i-1] * suffix[i+1])

        return res