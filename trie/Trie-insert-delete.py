class Trie:
    def __init__(self):
        self.root = Node("")
    def search_prefix(self, key):
		chars = []
        cur = self.root
        for i,x in enumerate(key):
            if x not in cur.children:
                return i-1,cur
            else:
                cur = cur.children[x]
				chars.append(x)
        return i,cur, chars
    def insert(self, key):
        i, node, chars = self.search_prefix(key)
        i += 1
        while i < len(key):
            node.children[key[i]] = Node(key[i])
            node = node.children[key[i]]
            i += 1
        node.terminal = True
    def _delete(self, root, key, i):
        print(root.key, root.children, key, i, key[i])
        if i == len(key)-1:
            if key[i] in root.children and root.children[key[i]].terminal == True:
                if len(root.children[key[i]].children) == 0:
                  del root.children[key[i]]
                  return True
                else:
                    root.children[key[i]].terminal = False
        else:
            if key[i] in root.children:
                x = self._delete(root.children[key[i]], key, i+1)
                if x == True and root.children[key[i]].terminal == False:
                    del root.children[key[i]]
                    return True
        return False
    def delete(self, prefix):
        self._delete(self.root, prefix, 0)
    def longest_prefix(self, prefix):
        cur= self.root
        last = None
        for x in prefix:
            if cur.terminal == True:
                last = cur
            if x in cur.children:
                cur = cur.children[x]
            else:
                return last
        return None
    def find_words(self, prefix):
        # get node from prefix
        i, node, chars = self.search_prefix(prefix)
        # every node after and this node is a valid word
        words = []
		if node.terminal == True:
			words.append("".join(chars))
		