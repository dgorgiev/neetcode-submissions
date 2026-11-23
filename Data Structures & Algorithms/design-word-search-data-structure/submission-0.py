class TreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children.update({c : TreeNode()})
                node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(node, i):
            if i == n:
                return node.isWord

            c = word[i]

            if c == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            else:
                if c in node.children:
                    return dfs(node.children[c], i+1)
            return False
            
        return dfs(self.root, 0)

