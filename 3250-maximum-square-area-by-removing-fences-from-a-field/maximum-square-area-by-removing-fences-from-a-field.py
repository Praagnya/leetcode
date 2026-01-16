from typing import List

class Solution:
    def get_edges(self, fences: List[int], border: int) -> set:
        # Include the two borders and sort all fence positions
        points = sorted([1] + fences + [border])
        
        # Compute all possible distances between any two fences
        edges = set()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.add(points[j] - points[i])
        
        return edges

    def maximizeSquareArea(
        self, 
        m: int, 
        n: int, 
        hFences: List[int], 
        vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7

        # Get all possible horizontal and vertical distances
        h_edges = self.get_edges(hFences, m)
        v_edges = self.get_edges(vFences, n)

        # Find the largest distance common to both directions
        common_edges = h_edges & v_edges
        if not common_edges:
            return -1

        max_edge = max(common_edges)
        return (max_edge * max_edge) % MOD