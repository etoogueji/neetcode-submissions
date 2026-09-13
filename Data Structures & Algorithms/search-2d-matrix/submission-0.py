class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, (ROWS * COLS) - 1

        while left <= right:
            mid = (left + right) // 2
            # Map 1D index mid to 2D coordinates (r, c)
            r, c = mid // COLS, mid % COLS
            
            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False