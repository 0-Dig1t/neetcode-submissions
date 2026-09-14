class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        s = s.lower().strip()
        alphabet = set("abcdefghijklmnopqrstuvwxyz0123456789")
        left, right = 0, len(s)-1

        while left <= right:
            while left < len(s) and s[left] not in alphabet:
                left += 1
            while right > 0 and s[right] not in alphabet:
                right -= 1
            if left < len(s) and right > 0 and s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True