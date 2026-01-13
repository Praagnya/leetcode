class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        totalArea = 0
        low = float('inf')
        high = 0
        
        for x, y, l in squares:
            totalArea += l * l
            low = min(low, y)
            high = max(high, y + l)
        
        target = totalArea / 2
        
        def area_below(y_line):
            area = 0.0
            for _, y, l in squares:
                if y_line <= y:
                    continue
                elif y_line >= y + l:
                    area += l * l
                else:
                    area += (y_line - y) * l
            return area
        
        left, right = low, high
        for _ in range(60):  # enough for 1e-5 precision
            mid = (left + right) / 2
            if area_below(mid) < target:
                left = mid
            else:
                right = mid
        
        return left