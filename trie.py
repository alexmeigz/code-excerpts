# Trie Class Definition
# '*' indicates end of string

class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, s: str):
        traverse = self.root
        
        for char in s:
            if not traverse.get(char):  
                traverse[char] = dict()
            traverse = traverse.get(char)
        
        traverse['*'] = '*'

    def find(self, s: str) -> bool:
        traverse = self.root
        
        for char in s:
            if not traverse.get(char):
                return False
            traverse = traverse.get(char)
        
        return traverse.get('*', '') == '*'

    def delete(self, s: str) -> bool:
        traverse = self.root
        
        for char in s:
            if not traverse.get(char):
                return False
            traverse = traverse.get(char)
        
        if not traverse.get('*'):
            return False
        
        traverse.pop("*")
        return True

    
'''
# Sample Usage 
if __name__ == "__main__":
    t = Trie()
    t.insert("hello")
    print(t.find("he"))
    t.insert("he")
    print(t.find("he"))
    t.delete("he")
    print(t.find("he"))
    print(t.root)
'''