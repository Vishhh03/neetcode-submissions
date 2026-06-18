class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        def checkRow(c):
            seen = set()
            for r in range(rows):
                if board[c][r] in seen:
                    return False
                elif board[c][r] ==".":
                    continue
                seen.add(board[c][r])
            return True
        def checkCol(r):
            seen = set()
            for c in range(rows):
                if board[c][r] in seen:
                    return False
                elif board[c][r] ==".":
                    continue
                seen.add(board[c][r])
            return True
            
        def checkSubBox(r,c):
            seen = set()
            for i in range(3):
                for j in range(3):
                    if board[r+i][c+j] in seen:
                        return False
                    elif board[r+i][c+j] ==".":
                        continue
                    seen.add(board[r+i][c+j])
            return True

        for i in range(rows):
            for j in range(cols):
                bool1 = checkRow(i) and checkCol(j)
                if i%3 == 0 and j%3==0:
                    bool2 = checkSubBox(i,j)
                    if not bool2:
                        return False
                if not bool1:
                    return False
        return True