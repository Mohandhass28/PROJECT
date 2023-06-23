class Solution(object):
    class Trie:
        class TrieNode(object):
            def __init__(self, word=''):
                self.letter = word
                self.word = [None] * 26
                self.end = False
        def __init__(self):
            self.root = self.TrieNode()
        def insert_word(self,word):
            root = self.root
            for i in word:
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
            cur = root
            curword = ''
            out = []
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
            return out

    def suggestedProducts(self, products, searchWord):
        products = sorted(products)
        out = []
        root = self.Trie()
        for i in products:
            root.insert_word(i)
        for i in range(len(searchWord)):
            words = root.search(searchWord[:i+1],root.root)
            out.append(words)
        return out

s = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
l = s.suggestedProducts(products,searchWord)
print(l)