class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums)
        gap = 0
        #n = len(sorted_arr)
        for i in range(len(sorted_arr) - 1):
            diff = sorted_arr[i+1] - sorted_arr[i]
            gap = max(gap, diff)

        return gap