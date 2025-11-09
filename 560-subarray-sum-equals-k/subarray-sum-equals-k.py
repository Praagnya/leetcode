class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}   # prefix sum count map
        count = 0
        rsum = 0
        
        for num in nums:
            rsum += num
            z = rsum - k
            
            if z in mp:
                count += mp[z]
            
            # update prefix sum frequency
            mp[rsum] = mp.get(rsum, 0) + 1
        
        return count