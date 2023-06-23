class Solution(object):
    class Trie:
        class TrieNode(object):
            def __init__(self, word=''):
                self.letter = word
                self.word = [None] * 26
                self.end = False
                self.hasset = set()
        def __init__(self):
            self.root = self.TrieNode()
        def insert_word(self,word,root):
            root = root
            word = word.lower()
            for i in word:
                if i.isalpha():
                    ind = ord(i) - ord('a')
                    if root.word[ind] == None:
                        root.word[ind] = self.TrieNode(i)
                    root = root.word[ind]
            root.end = True

        def get(self,root):
            nai = []
            for i in root.word:
                if i != None:
                    nai.append(i)
            return nai
        def search(self,wor,root):
            root.hasset.add(wor)
            cur = root
            curword = ''
            out = []
            wor = wor.lower()
            for i in wor:
                ind = ord(i) - ord('a')
                if cur.word[ind] != None:
                    cur = cur.word[ind]
                    curword += cur.letter
                else:
                    return []
            def dfs(ro,wor):
                if ro.end == True:
                    out.append(wor)
                for i in self.get(ro):
                    dfs(i,wor+i.letter)
            dfs(cur,curword)
            new = []
            for i in out:
                if i in root.hasset:
                    new.append(i)
            new.extend(out[:7])
            new = set(new)
            return new

    def suggestedProducts(self, products, searchWord=None):
        products = sorted(products)
        print(products)
        out = []
        root = self.Trie()
        for i in products:
            root.insert_word(i,root)
        for i in range(len(searchWord)):
            words = root.search(searchWord[:i+1],root.root)
            out.append(words)
        return out


def search_engine():
    s = Solution()
    out = []
    with open('New Text Document.txt','r+') as file:
        out.append(file.read())
    out = out[0].split()
    root = s.Trie.TrieNode()
    no = s.Trie()
    out = sorted(out)
    for i in out:
        if i.isalpha():
            no.insert_word(i.lower(),root)
    while True:
        n = input('Type: ')
        if n.lower() == 'quit':
            break
        words = no.search(n.lower(),root)
        no.insert_word(n,root)
        with open('NEw','a') as fise:
            fise.write(n)
        for i in words:
            print(i)

search_engine()
