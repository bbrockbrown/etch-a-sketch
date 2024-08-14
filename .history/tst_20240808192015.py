def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        rows = []
        cols = []
        for i in range(n):
            currRow = []
            for j in range(n):
                if board[i][j] not in currRow or board[i][j] == ".":
                    currRow.append(board[i][j])
                else:
                    return False
            print(f"{i+1}:", currRow)
            if currRow not in rows or currRow == [".",".",".",".",".",".",".",".","."]:
                rows.append(currRow)
            else:
                return False

        for k in range(n):
            currCol = []
            for m in range(n):
                if board[m][k] not in currCol or board[m][k] == ".":
                    currCol.append(board[m][k])
                else:
                    return False
            if currCol not in cols:
                cols.append(currCol)
            else:
                return False
        return True
    
    
print(isValidSudoku([[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))