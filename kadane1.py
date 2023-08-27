class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        max_f = arr[0]
        max_e = arr[0]
        for i in range(1,N):
            max_e = max_e + arr[i]
            if (max_f < max_e):
                max_f = max_e
            if (max_e < 0):
                max_e = 0
            
        return max_f


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()