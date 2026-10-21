class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            x, y = numbers[left], numbers[right]
            if x + y > target:
                right -= 1
            elif x + y < target:
                left += 1
            else:
                break

        return [left+1, right+1]