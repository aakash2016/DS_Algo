## Day 2
## Binary Search Trees
class Node:
	def __init__(self, data):
		self.data = data
		self.leftchild = None
		self.rightchild = None

class bst:
	def __init__(self):
		self.root = None

	def insert(self, data):		
		if self.root == None:
			self.root = Node(data)

		else:
			self.insertnode(data, self.root) 
		
	def insertnode(self, data, node):
		if data < node.data:
			if node.leftchild:
				self.insertnode(data, node.leftchild)
			else:
				node.leftchild = Node(data)

		else:
			if node.rightchild:
				self.insertnode(data, node.rightchild)
			else:
				node.rightchild = Node(data)

	def getminval(self):
		if self.root:
			return self.getmin(self.root)

	def getmin(self, node):
		if node.leftchild:
			return self.getmin(node.leftchild)
		return node.data

	def getmaxval(self):
		if self.root:
			return self.getmax(self.root)

	def getmax(self, node):
		if node.rightchild:
			return self.getmax(node.rightchild)
		return node.data

	def traverse(self):
		if self.root:
			self.traverseinorder(self.root)	
				
	def traverseinorder(self, node):
		if node.leftchild:
			self.traverseinorder(node.leftchild)	
		
		print(node.data)
		
		if node.rightchild:
			self.traverseinorder(node.rightchild)

	def remove(self, data):
		if self.root:
			self.root = self.removenode(data, self.root)

	def removenode(self, data, node):		
		if data < node.data:
			node.leftchild = self.removenode(data, node.leftchild)
	
		elif data > node.data:
			node.rightchild = self.removenode(data, node.rightchild)	
		
		else:
			if not node.leftchild and not node.rightchild:
				print("removing a leaf node ..")
				del node 	
				return None
			
			if not node.leftchild:
				print("removing node with single right child")				
				tempnode = node.rightchild	
				del node
				return tempnode					
				
			elif not node.rightchild:
				print("removing node with single left child")
				tempnode = node.leftchild
				del node
				return tempnode
		
			else:
				print("removing node with 2 children")
				tempnode = self.getpred(node.leftchild)	
				node.data = tempnode.data
				node.leftchild = self.removenode(tempnode.data, node.leftchild)
		return node

	def getpred(self, node):
		if node.rightchild:
			return self.getpred(node.rightchild)
		return node

bt = bst()
bt.insert(12)
bt.insert(4)
bt.insert(1)
bt.insert(5)
bt.insert(20)
bt.remove(4)

print(bt.getminval())
print(bt.getmaxval())
bt.traverse()

#bt = bst()
#bt.insert("C")
#bt.insert("S")
#bt.insert("A")
#bt.insert("D")
#bt.traverse()
