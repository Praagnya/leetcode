class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0 : -1} # {remainder:remainder_index}
        r_sum = 0 
        
        for i, num in enumerate(nums): 
            r_sum += num
            rem = r_sum % k

            if rem in remainder_index: 
                if i - remainder_index[rem] >= 2: 
                    return True 
            else:
                remainder_index[rem] = i
        
        return False 
        
        # Brute force: 
        # n = len(nums)
        # for start in range(n - 1): 
        #     r_sum = nums[start]
        #     for end in range(start + 1, n): 
        #         r_sum += nums[end]

        #         if r_sum % k == 0:
        #             return True 
                 
        # return False 