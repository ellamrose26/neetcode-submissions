class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned+= ch.lower()
        print(cleaned)
        
        reversed_string = cleaned[::-1]
        if cleaned == reversed_string:
            return True
        else:
            return False