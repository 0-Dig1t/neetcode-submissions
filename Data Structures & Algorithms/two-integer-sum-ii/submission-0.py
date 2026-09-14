class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using a left and right pointer
        # left at the start and right at the end
        # while the pointers don't cross check 
        # if the elements at the pointers equal target
        # then return the index at the pointers
        # if sum < target, left += 1
        # if sum > target, right -= 1
        l, r = 0, len(numbers)-1
        while l < r:
            currSum = numbers[l] + numbers[r]    
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l+1, r+1]
        
        return []