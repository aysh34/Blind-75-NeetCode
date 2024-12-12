class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def find(i,j,idx):
            if idx == len(word):
                return True
            if i<0 or i>= rows or j<0 or j>=cols or board[i][j] != word[idx]:
                return False
                 
            temp = board[i][j] 
            board[i][j] = '$' # visited current cell

            # explore all 4 directions
            found = find(i+1, j ,idx+1) or find(i-1, j ,idx+1) or find(i, j+1 ,idx+1) or find(i, j-1 ,idx+1)

            board[i][j] = temp
            return found


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and find(i,j,0):
                    return True
        return False