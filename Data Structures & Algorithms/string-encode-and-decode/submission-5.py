class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:

            for char in word:
                val = ord(char)
                res.append(str(val))

            res.append("/")

        return ' '.join(res)
    
    def decode(self, s: str) -> List[str]:
        res = []

        curr = []
        for char in s.split(' '):
            if char == '/':
                res.append(''.join(curr))
                curr = []
                continue
            elif char != '':
                curr.append(chr(int(char)))

        return res