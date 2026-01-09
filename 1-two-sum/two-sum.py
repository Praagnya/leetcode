class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target -n], i]
            seen[n] = i  
        
        
        
        
        # # brute force 
        # # time: O(n2)
        # # space: o(n)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target: 
        #             return i, j 
