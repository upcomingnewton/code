class Node:
	def __init__(self, key, terminal=False):
		self.key = key
		self.terminal = terminal
		self.children = {}
		self.num = 0
	
class Trie:
	def __init__(self):
		self.root = Node("")
	def insert(self, prefix):
		cur = self.root
		for x in prefix:
			if x not in cur.children:
				cur.children[x] = Node(x)
			cur.num += 1
			cur = cur.children[x]
		cur.terminal = True
	
	def longest_prefix(self, words):
		for i in range(len(words)-1):
			if words[i][0] != words[i+1][0]:
				return ""
		x = words[0][0]
		if x not in self.root.children:
			return ""
		chars = []
		cur = self.root.children[x]
		while len(cur.children) == 1:
			chars.append(cur.key)
			cur = cur.children[list(cur.children.keys())[0]]
		chars.append(cur.key)
		return "".join(chars)
		

def main():
	t = Trie()
	t.insert("geeksforgeeks")
	t.insert("geeks")
	t.insert("geek")
	t.insert("geezer")
	print(t.longest_prefix(["geeksforgeeks", "geeks", "geek", "geezer"]))
	p = ["apple", "ape", "april"]
	for x in p:
		t.insert(x)
	print(t.longest_prefix(p))
		
