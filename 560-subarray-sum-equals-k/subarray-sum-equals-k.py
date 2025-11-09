class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}   # prefix sum count map
        count = 0
        rsum = 0
        
        for num in nums:
            rsum += num
            
            if rsum - k in mp:
                count += mp[rsum - k]
            
            # update prefix sum frequency
            mp[rsum] = mp.get(rsum, 0) + 1
        
        return count