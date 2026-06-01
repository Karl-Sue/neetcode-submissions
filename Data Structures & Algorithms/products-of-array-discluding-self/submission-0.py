class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums)):
            prefix = [x for x in nums[0:i]]
            suffix = [x for x in nums[i+1:len(nums)]]
            product = prefix + suffix
            a = 1
            for k in product:
                a*=k
            result.append(a)
        return result