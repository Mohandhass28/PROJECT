class Sudoku:
    def __init__(self,mat):
        self.mat = mat

    #THE MANI BACKTRACK ALGO
    def Back_tracking(self):
        mat = self.mat
        rc = self.getemty()
        if rc == None:
            return True
        r,c = rc
        for i in range(1,10):
            if self.row(rc,str(i)) and self.colume(rc,str(i)) and self.mate(rc,str(i)):
                mat[r][c] = str(i)
                self.print()
                if self.Back_tracking():
                    return True
                mat[r][c] = '.'


    #CHECKING IN COLUMN FOR I
    def row(self,rowc,i):
        mat = self.mat
        row,col = rowc
        def dfs(r,c):
            if mat[r][c] == i:
                return False
            if r >= len(mat)-1:
                return True
            return dfs(r+1,c)
        return dfs(0,col)

    def print(self):
        for i in self.mat:
            print(i)


    #CHECKING COLUMN FOR I
    # I IS THE GET BY BACKTRACKING FUNCTION
    def colume(self,col,i):
        mat = self.mat
        row,co = col
        def dfs(r,c):
            if mat[r][c] == i:
                return False
            if c >= len(mat)-1:
                return True
            return dfs(r,c+1)
        return dfs(row,0)

    #CHECKING THE 3X3 MATRIX FOR I
    def mate(self,rc,i):
        mat = self.mat
        r,c = rc
        star = r - r % 3
        end  = c - c % 3
        for k in range(3):
            for j in range(3):
                if mat[star+k][end+j] == i:
                    return False
        return True

    #FINDING THE EMPTY ROW AND COLUMN IN THE BOAD
    def getemty(self):
        mat = self.mat
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == '.':
                    return (i,j)
        return None


board =  [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

s = Sudoku(board)
s.Back_tracking()