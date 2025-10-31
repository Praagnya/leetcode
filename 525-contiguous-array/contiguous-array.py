class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        rsum = 0
        max_len = 0
        first = {0: -1}

        for i, x in enumerate(nums):
            rsum += 1 if x == 1 else -1 
            if rsum in first: 
                max_len = max(max_len, i - first[rsum])
            else: 
                first[rsum] = i
        return max_len 