class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        largest = max(nums)
        smallest = min (nums)
        lst = {}
        max_count = 0
        count = 0
        for i in range(smallest,largest+1):
            lst[i] = 0;
        for i in range(0,len(nums)):
            lst[nums[i]] = lst.get(nums[i],0) + 1
        for key,value in lst.items():
            if value != 0:
                count+=1
            else:
                if count > max_count:
                    max_count = count
                count = 0
        if count > max_count:
            max_count = count
        return max_count
        