class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        for m in range(n):
            while i < n and not s[i].isalnum():
                i+=1
            while j >= 0 and not s[j].isalnum():
                j-=1
            
            if i >= n and j < 0:
                break

            if s[i].lower() != s[j].lower():
                return False
            if i >= j or i >= n-1:
                break
            i+=1
            j-=1
            
        return True


        