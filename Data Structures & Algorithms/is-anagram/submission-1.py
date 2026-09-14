from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s, freq_t = defaultdict(int), defaultdict(int)

        for char in s:
            freq_s[char] += 1
        for char in t:
            freq_t[char] += 1

        return freq_s == freq_t