class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] < curr:
                arr[i] = curr
            arr[i], curr = curr, arr[i]
            
        return arr