class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if (target == nums[i]):
                return i
        
        if target not in nums:
            last = len(nums)-1
            for i in range(len(nums)):
                if (target < nums[i]):
                    return i
                if (target > nums[i] and target < nums[i+1]):
                    return i+1
                else:
                    if (target > nums[-1]):
                        return last + 1