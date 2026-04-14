class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            differ = target - n
            if differ in seen:
                return [seen[differ], i]
            seen[n] = i