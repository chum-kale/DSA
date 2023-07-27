class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if (n < 2):
            return 0

        for i in range(n):
            if (self.is_prime(i)):
                count += 1
        
        return count

    def is_prime(self, x: int) -> bool:
        if (x < 2):
            return False 

        for j in range(2, x):
            if (x % j == 0):
                return False
            
        return True
    

def main():
    sol = Solution()
    n = 3  # Change this value to the desired number for which you want to count primes
    result = sol.countPrimes(n)
    print(f"The number of primes less than {n} is: {result}")

if __name__ == "__main__":
    main()