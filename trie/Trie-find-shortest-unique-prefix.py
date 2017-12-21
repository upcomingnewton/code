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
		
		def _shortest_unique_prefix(self, root):
			if root.num < 2:
				return [root.key]
			else:
				chars = []
				for x in root.children:
					chars.extend(self._shortest_unique_prefix(root.children[x]))
				print(chars)
				return [root.key + x for x in chars]
			
		def find_shortest_unique_prefix(self):
			return self._shortest_unique_prefix(self.root)
	
	def main():
		t = Trie()
		t.insert("zebra")
		t.insert("dog")
		t.insert("duck")
		t.insert("dove")
		print(t.find_shortest_unique_prefix())
		
	if  __name__ == "__main__":
