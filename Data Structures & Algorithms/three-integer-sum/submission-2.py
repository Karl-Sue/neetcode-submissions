class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p1 = 0
        p2 = len(nums) - 1
        result = []
        while p1 <= p2 - 2:
            p3 = p2
            while p3 >= p1 + 2:
                if -(nums[p1]+nums[p2]) in nums[p1+1:p2]:
                    p3 = p3 - 1
                    while -(nums[p1]+nums[p2]) != nums[p3]:
                        p3 = p3 - 1
                    a = [nums[p1], nums[p2], nums[p3]]
                    a.sort()
                    if a not in result: 
                        result.append(a)
                p2 -= 1
                p3 = p2
            p1 += 1
            p2 = len(nums) - 1
        return result
