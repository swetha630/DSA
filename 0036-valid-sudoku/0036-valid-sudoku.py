class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[[False]*9 for _ in range(9)]
        c=[[False]*9 for _ in range(9)]
        b=[[False]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    val=int(board[i][j])-1 
                    bi=(i//3)*3+(j//3)
                    if r[i][val] or c[j][val] or b[bi][val]:
                        return False 
                    r[i][val]=c[j][val]=b[bi][val]=True 
        return True
            