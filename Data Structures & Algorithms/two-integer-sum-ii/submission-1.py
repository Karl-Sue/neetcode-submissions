class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        p1 = 0
        p2 = l - 1
        while numbers[p1] + numbers[p2] != target and p1 != p2:
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
        return [p1+1, p2+1]