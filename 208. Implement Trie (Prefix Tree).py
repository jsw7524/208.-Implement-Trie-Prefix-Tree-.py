class Node(object):
    def __init__(self,c):
        self.ch=c
        self.branch={}

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stone=Node('^')
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        data=list('^'+word+'$')
        self.insertRecurively(self.stone, data)
        
    def insertRecurively(self, node, data):
        if len(data)>0:
            if data[0] not in node.branch:
                node.branch[data[0]]=Node(data[0])
            self.insertRecurively(node.branch[data[0]],data[1:])
          
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.startsWith(word+'$')

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        data=list('^'+prefix)
        return self.startsWithRecurively(self.stone, data)
        
    def startsWithRecurively(self, node, data):
        if len(data)>0:
            if data[0] not in node.branch:
                return False
            return self.startsWithRecurively(node.branch[data[0]],data[1:])
        return True
        


trie = Trie();
trie.insert("apple");
trie.insert("april");
assert True==trie.search("apple"); 
assert False==trie.search("app");     
assert True ==trie.startsWith("app"); 
trie.insert("app");   
assert True==trie.search("app");   
