class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isFinal = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                curr.chars[c] = TrieNode()
            curr = curr.chars[c]
        
        curr.isFinal = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]

        return curr.isFinal
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.chars:
                return False
            curr = curr.chars[c]

        return True
        
        