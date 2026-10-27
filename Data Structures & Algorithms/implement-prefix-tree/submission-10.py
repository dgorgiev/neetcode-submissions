class TreeNode():
    def __init__(self):
        self.children = {}
        self.valid = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        self.valid = False

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children.update({c : TreeNode()})
            node = node.children.get(c)
        node.valid = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            node = node.children.get(c, False)
            if not node:
                return False
        return node.valid

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if node is None:
                return False
        
        return True
        
                    
        