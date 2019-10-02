class Node():
    def __init__(self, val=None):
        self.children = {}
        self.value = val
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = Node()
    
    def find(self, key):
        pass

    def search(self,word):
        current = self.root
        for i in range(len(word)):
            if word[i] not in current.children:
                return False
            else:
                current = current.children[word[i]]
        return True if current.isWord else False

    def add(self,word):
        current = self.root
        i = 0
        while i < len(word):
            if word[i] in current.children:
                current = current.children[word[i]]
                i += 1
            else: #Node for that letter wasn't found - Add node(s)
                break
        #append new nodes for remaining characters
        while i < len(word):
            current.children[word[i]] = Node(word[i])
            current = current.children[word[i]]
            i += 1
        current.isWord = True

    def delete(self,word):
        current = self.root
        i = 0
        while i < len(word):
            if word[i] in current.children:
                current = current.children[word[i]]
                i += 1
            else: #Node for that letter wasn't found - Add node(s)
                return False
        current.isWord = False


t = Trie()
t.add('Cow')
t.add('Cower')
