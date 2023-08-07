class Solution:
    def segregateElements(self, arr, n):
        negs, posi = 0, n-1
        while negs<=posi:
            if (arr[negs]<0):
                arr.append(arr.pop(negs))
                posi -= 1
            else:
                negs += 1
                
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()