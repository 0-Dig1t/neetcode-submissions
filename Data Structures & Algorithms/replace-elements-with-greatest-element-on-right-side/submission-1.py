class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < curr:
                arr[i] = curr
            arr[i], curr = curr, arr[i]
            
        return arr