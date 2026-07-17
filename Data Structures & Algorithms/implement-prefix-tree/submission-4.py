class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True
        
        