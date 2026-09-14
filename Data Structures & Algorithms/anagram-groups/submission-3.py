from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            vec = [0] * 26
            for c in s:
                val = ord(c) - ord('a')
                vec[val] += 1
            map[tuple(vec)].append(s)

        return list(map.values())