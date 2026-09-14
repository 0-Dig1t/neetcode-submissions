class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fow = [1] * len(nums)
        bac = [1] * len(nums)
        res = []
        fow[0] = nums[0]
        bac[-1] = nums[-1]
        for i in range(1, len(nums)):
            fow[i] = fow[i-1] * nums[i]
        for j in range(len(nums)-2, -1, -1):
            bac[j] = bac[j+1] * nums[j]
        res.append(bac[1])
        for k in range(1, len(nums)-1):
            prod = fow[k-1] * bac[k+1]
            res.append(prod)
        res.append(fow[len(nums)-2])
        return res