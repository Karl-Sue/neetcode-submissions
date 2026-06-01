class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numList = {}
        result = []
        uniqueNum = set(nums)
        for num in nums:
            numList[num] = nums.count(num)
        numList = sorted(numList.items(),key=lambda x:x[1],reverse=True)
        for i in range(0,k):
            result.append(numList[i][0])
        return result