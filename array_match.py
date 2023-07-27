from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in temp:
                return [temp[other], i]
            temp[num] = i
        return []

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
result = sol.twoSum(nums, target)
print("Matching:", result)

