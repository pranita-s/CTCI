import collections
class Trie:
    DICT = 0
    END = 1

    def __init__(self):
        self.root = [{},False]
        
    def insert(self,word):
        _root = self.root
        for letter in word:
            if letter not in _root[Trie.DICT]:
                _root[Trie.DICT][letter] = [{},False]
            _root = _root[Trie.DICT][letter]
        _root[Trie.END] = True

    def findT9(self,num):
        d = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
             '9': 'wxyz'}
        result = []
        
        def helper(num,i,soFar,node):
            if i == len(num) and node[Trie.END] == True:
                result.append(soFar)
            else:
                if d[num[i]]:
                    for char in d[num[i]]:
                        if char in node[Trie.DICT]:
                            helper(num,i+1,soFar+char,node[Trie.DICT][char])
                else:
                    helper(num,i+1,soFar,node)
        helper(num,0,'',self.root)
        return result

t = Trie()
valid = ['tree','used']
for word in valid:
    t.insert(word)
print(t.findT9('8733'))

