class NQUEEN(object):
    def solveNQueens(self, n):
        leftdig = set()
        rightdig = set()
        boad = [['.'for _ in range(n)] for _ in range(n)]
        out = []
        def backtrack(row):
            if row > n-1:
                temp = []
                for i in boad:
                    string = ''.join(i)
                    temp.append(string)
                out.append(temp)
                return
            for col in range(n):
                rightdi = row - col
                leftdi = row + col
                if rightdi not in rightdig and leftdi not in leftdig and self.cherow(row, col, boad) and self.checol(
                        row, col, boad):
                    leftdig.add(row + col)
                    rightdig.add(row - col)
                    boad[row][col] = 'Q'
                    backtrack(row + 1)
                    leftdig.remove(row + col)
                    rightdig.remove(row - col)
                    boad[row][col] = '.'

        backtrack(0)
        return out

    # CHECKING ROW FOR THE QUEEN
    def cherow(self, row, col, boad):
        for i in range(len(boad)):
            if boad[i][col] == 'Q':
                return False
        return True
    #CHECKING COLUMN FOR THE QUEEN
    def checol(self, row, col, boad):
        for i in range(len(boad)):
            if boad[row][i] == 'Q':
                return False
        return True

s = NQUEEN()
l = s.solveNQueens(4)
print(l)