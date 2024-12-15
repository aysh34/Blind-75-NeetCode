class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first build the trie through words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                idx = ord(char) - ord('a')
                if not node.children[idx]:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
            node.word = word

        def backtrack(i,j,node):
            char = board[i][j]

            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return
            next_node = node.children[idx]

            if next_node.word:
                res.add(next_node.word)
                next_node.word = None # avoid duplicates

            # explore in all 4 directions
            board[i][j] = '$' # visited

            for x , y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<rows and 0<=y<cols and board[x][y] != '$':
                    backtrack(x,y,next_node)
            board[i][j] = char

        rows = len(board)
        cols = len(board[0])
        res = set()
        for i in range(rows):
            for j in range(cols):
                backtrack(i,j,root)
        
        return list(res)