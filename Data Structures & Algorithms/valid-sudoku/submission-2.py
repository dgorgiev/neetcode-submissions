class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_list(l: List[str]) -> bool:
            nums = [val for val in l if val != "."]
            return len(set(nums)) == len(nums)
        for i in board:
            if not valid_list(i):
                return False
        for i in range(9):
            col = list()
            for j in range(9):
                col.append(board[j][i])
            if not valid_list(col):
                return False
        for i in range(0, 9, 3):
            square = list()
            for m in range(3):
                for n in range(3):
                    square.append(board[n+(i%3)*3][m+(i//3)*3])
            if not valid_list(square):
                return False
        return True
    
    
