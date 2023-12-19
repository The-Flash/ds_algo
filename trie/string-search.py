class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True

    def startswith(self, prefix):
        cur: TrieNode = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    def search(self, word):
        cur: TrieNode = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEndOfWord

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("pineapple")
    trie.insert("banana")
    trie.insert("mango")
    trie.insert("grapes")

    print(trie.startswith("app"))
    print(trie.search("apple"))
