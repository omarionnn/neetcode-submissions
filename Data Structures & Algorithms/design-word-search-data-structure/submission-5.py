class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node

            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for kid in curr.children.values():
                        if dfs(i + 1, kid):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False

                    curr = curr.children[c]

            return curr.endOfWord

        return dfs(0, self.root)
        
