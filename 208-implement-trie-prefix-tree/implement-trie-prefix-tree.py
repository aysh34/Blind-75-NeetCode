class Trie:
    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.children = [None] * 26

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a') # the index of a character relative to 'a'
            if not node.children[idx]:
                node.children[idx] = self.TrieNode()
            node = node.children[idx]
        node.isEnd = True # end of the valid word
        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.isEnd 

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
# TC = O(L) L is the length of word/prefix


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)