class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1

        while low <= high:
            mid = (low + high) // 2

            
            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                # Target is in the range for this row; search the row
                row = matrix[mid]
                left, right = 0, len(row) - 1
                while left <= right:
                    m = (left + right) // 2
                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        left = m + 1
                    else:
                        right = m - 1
                # If not found in the row
                return False

        # Target not found in any row
        return False
             
        