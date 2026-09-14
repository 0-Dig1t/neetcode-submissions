class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            enc = ''
            for letter in word:
                enc += str(ord(letter))
                enc += ' '
            res += enc
            res += ','
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        out = []
        inp = s.split(',')[:-1]
        for string in inp:
            newString = string.split(' ')[:-1]
            res.append(newString)
        for string in res:
            word = ''
            for letter in string:
                print(int(letter))
                word += chr(int(letter))
            out.append(word)
        return out