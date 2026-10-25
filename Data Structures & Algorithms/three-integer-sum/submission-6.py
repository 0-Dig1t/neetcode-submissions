class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr = [nums[i], nums[left], nums[right]]
                currSum = sum(curr)
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    res.append(curr)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
            
        return res