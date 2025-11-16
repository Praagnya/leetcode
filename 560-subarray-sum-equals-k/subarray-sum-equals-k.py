class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0: 1} # {running_sum: frequency} allows counting subarray that starts from index 0
        count = 0 
        r_sum = 0 

        for i in nums: 
            r_sum += i

            # check if running sum is in map and keep a count 
            if r_sum - k in map: 
                count += map[r_sum - k]
             
            # add the running sum to map for further check
            map[r_sum] = map.get(r_sum, 0) + 1 # map.get will return r_sum if there else o
        
        return count 
        
        """
        Brute force, we are using nested loops.
        Time Complexity: 0(n**2)
        """
        # count = 0
        # n = len(nums)

        # for start in range(n): #loop through all the elements
        #     current_sum = 0
            
        #     for end in range(start, n):
        #         current_sum += nums[end]
            
        #         if current_sum == k:
        #             count += 1

        # return count

