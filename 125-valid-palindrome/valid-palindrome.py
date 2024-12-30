class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        left = 0
        right = len(new) - 1
        while left < right:
            if new[left] != new[right]:
                return False
            left +=1
            right -=1

        return True