class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.isEndOfWord

            # check all possible children
            if word[idx] == ".":
                for child in node.children:
                    if child and dfs(child, idx + 1):
                        return True
            else:
                child_idx = ord(word[idx]) - ord('a') 
                if node.children[child_idx]:
                    return dfs(node.children[child_idx], idx + 1)

            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)