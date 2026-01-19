class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build prefix sum array
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                    + mat[i][j]
                )

        # Check if any k x k square has sum <= threshold
        def can_form(k: int) -> bool:
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    square_sum = (
                        prefix[i + k][j + k]
                        - prefix[i][j + k]
                        - prefix[i + k][j]
                        + prefix[i][j]
                    )
                    if square_sum <= threshold:
                        return True
            return False

        # Binary search on side length
        left, right = 0, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_form(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans