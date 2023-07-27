class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        rev = y[::-1]
        if (y == rev):
            print("true")
        else:
            print("false")


x = -121
sol = Solution()
sol.isPalindrome(x)