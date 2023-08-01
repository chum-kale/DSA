class Solution:
    def reverse(self, x: int) -> int:
        maxi = 2**31 - 1
        num = x
        rev = 0
        while (x != 0):
            r = x%10
            rev = rev*10 + r
            x //= 10

        if (rev > maxi):
            return 0

        if (num < 0):
            return -rev
        
        return rev
    
def main():
    sol = Solution()

    # Test cases
    num1 = -123
    result1 = sol.reverse(num1)
    print("Reversed number:", result1)  # Output: 321

    num2 = -123
    result2 = sol.reverse(num2)
    print("Reversed number:", result2)  # Output: -321

    num3 = 120
    result3 = sol.reverse(num3)
    print("Reversed number:", result3)  # Output: 21

    num4 = 1534236469
    result4 = sol.reverse(num4)
    print("Reversed number:", result4)  # Output: 0 (Exceeds 32-bit integer range)


if __name__ == "__main__":
    main()