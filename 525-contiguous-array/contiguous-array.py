class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        rsum = 0
        max_value = 0
        map = {0: -1}

        for i, x in enumerate(nums):
            rsum += 1 if x == 1 else -1 
            if rsum in map: 
                max_value = max(max_value, i - map[rsum])
            else: 
                map[rsum] = i
        return max_value