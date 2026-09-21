class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        suffix = [1] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]
        suffix.append(1)

        prefix = 1
        for i in range(len(nums)):
            res.append(prefix*suffix[i+1])
            prefix *= nums[i]

        return res