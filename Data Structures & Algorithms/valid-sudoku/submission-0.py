class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(list)
        columns = defaultdict(list)
        subbox = defaultdict(list)

        for row in range(len(board)):


            for column in range(len(board[row])):

                subboxNum = ((row // 3) - 1) + 3 * ((column // 3) - 1)

                subbox

                if (board[row][column] == "."):
                    pass
                elif (board[row][column] in rows[row]) or (board[row][column] in columns[column]) or (board[row][column] in subbox[subboxNum]):
                    return False
                else: 
                    rows[row].append(board[row][column])
                    columns[column].append(board[row][column])
                    subbox[subboxNum].append(board[row][column])
        
        return True











