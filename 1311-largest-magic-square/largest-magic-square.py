class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # row prefix sums
        rowPref = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            s = 0
            for j in range(n):
                s += grid[i][j]
                rowPref[i][j + 1] = s

        # col prefix sums
        colPref = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            s = 0
            for i in range(m):
                s += grid[i][j]
                colPref[i + 1][j] = s

        # main diagonal prefix (\): diag1Pref[i+1][j+1] depends on diag1Pref[i][j]
        diag1Pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                diag1Pref[i + 1][j + 1] = grid[i][j] + diag1Pref[i][j]

        # anti-diagonal prefix (/): diag2Pref[i+1][j] depends on diag2Pref[i][j+1]
        diag2Pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                diag2Pref[i + 1][j] = grid[i][j] + diag2Pref[i][j + 1]

        def row_sum(r: int, c: int, k: int) -> int:
            return rowPref[r][c + k] - rowPref[r][c]

        def col_sum(r: int, c: int, k: int) -> int:
            return colPref[r + k][c] - colPref[r][c]

        def diag1_sum(r: int, c: int, k: int) -> int:
            return diag1Pref[r + k][c + k] - diag1Pref[r][c]

        def diag2_sum(r: int, c: int, k: int) -> int:
            # from (r, c+k-1) to (r+k-1, c)
            return diag2Pref[r + k][c] - diag2Pref[r][c + k]

        def is_magic(r: int, c: int, k: int) -> bool:
            target = row_sum(r, c, k)

            # diagonals
            if diag1_sum(r, c, k) != target:
                return False
            if diag2_sum(r, c, k) != target:
                return False

            # rows
            for i in range(r, r + k):
                if row_sum(i, c, k) != target:
                    return False

            # cols
            for j in range(c, c + k):
                if col_sum(r, j, k) != target:
                    return False

            return True

        max_k = min(m, n)
        for k in range(max_k, 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        return 1