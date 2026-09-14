class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}
        for i in range(len(strs)):
            bitString = [0] * 26
            for letter in strs[i]:
                index = ord(letter) - ord('a')
                bitString[index] += 1
            anaMap[str(bitString)] = [strs[i]] + anaMap.get(str(bitString), [])
        return anaMap.values()