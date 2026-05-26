class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ph = len(matrix)-1
        pl = 0

        while ph >= pl:
            pm = (ph+pl) // 2
            if matrix[pm][0] > target:
                ph = pm-1
            elif matrix[pm][len(matrix[pm])-1] < target:
                pl = pm+1
            else:
                break
        
        h = len(matrix[pm])
        l = 0

        while h>=l:
            m = (h+l) // 2
            if matrix[pm][m] > target:
                h = m-1
            elif matrix[pm][m] < target:
                l = m+1
            else:
                return True

        return False