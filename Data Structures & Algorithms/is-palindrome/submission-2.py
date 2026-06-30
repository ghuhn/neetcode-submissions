class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower=s.lower()
        a=""
        for i in s_lower:
            if i.isalnum():
                a+=i.lower()
        if a==a[::-1]:
            return True
        else:
            return False
