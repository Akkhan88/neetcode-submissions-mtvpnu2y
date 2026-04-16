class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] = count[n]+1 
            else:
                count[n] = 1 
        sorted_nums = sorted(count, key=count.get, reverse=True)
        return sorted_nums[:k]