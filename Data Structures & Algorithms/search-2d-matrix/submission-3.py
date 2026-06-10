class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, down = 0, rows - 1
        left, right = 0, cols - 1

        while top  <= down:
            row = (top + down) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                down = row - 1
            else:
                break


        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1

        return False

        