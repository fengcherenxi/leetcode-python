class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        if a[::-1]==a:
            return True
        else:
            return False