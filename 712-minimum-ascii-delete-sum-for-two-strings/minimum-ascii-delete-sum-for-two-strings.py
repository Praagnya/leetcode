
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        saved_result = {}

        def compute_cost(i, j):
            # if both strings are empty
            if i < 0 and j < 0: 
                return 0
        
            
            # if already computed 
            if (i,j) in saved_result: 
                return saved_result[(i,j)]
            
            # if s1 is empty
            if i < 0: 
                saved_result[(i,j)] = ord(s2[j]) + compute_cost(i, j-1)
                return saved_result[(i,j)]

            # if s2 is empty 
            if j < 0: 
                saved_result[(i,j)] = ord(s1[i]) + compute_cost(i-1, j)
                return saved_result[(i,j)]
            
            # if both strings are equal
            if s1[i] == s2[j]:
                saved_result[(i,j)] = compute_cost(i-1, j-1)

            else: 
                saved_result[(i,j)] = min(
                    ord(s1[i]) + compute_cost(i-1, j), 
                    ord(s2[j]) + compute_cost(i, j-1)
                    )
                
            return saved_result[(i, j)]

        return compute_cost(len(s1) -1, len(s2) -1)








        # def compute_cost(i, j):
        #     # when s1 is empty string, we delete all the characters from s2 
        #     if i < 0: 
        #         delete_cost = 0 
        #         for pointer in range(j+1):
        #             delete_cost += ord(s2[pointer])
        #         return delete_cost 
            
        #     # when s2 is empty, we delete all the characters from s1
        #     if j < 0: 
        #         delete_cost = 0 
        #         for pointer in range(i + 1):
        #             delete_cost += ord(s1[pointer])
        #         return delete_cost 
            
        #     # if both are equal 
        #     if s1[i] == s2[j]: 
        #         return compute_cost(i-1, j-1)
        #     else: 
        #         return min(
        #             ord(s1[i]) + compute_cost(i-1, j),
        #             ord(s2[j]) + compute_cost(i, j-1),
        #             ord(s1[i]) + ord(s2[j]) + compute_cost(i-1, j-1)
        #         )
        # return compute_cost(len(s1)-1, len(s2)-1)
