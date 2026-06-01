class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            difference = target - nums[i]
            if nums.count(difference)>1: return [i, nums.index(difference,i+1)]
            elif difference in nums and difference != nums[i]: return [i, nums.index(difference,i+1)]
            else: continue                                                 