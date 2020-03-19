# Day_1
## Linked Lists 
class node:
	def __init__(self, data):
		self.data = data
		self.nextnode = None

class linked_list: 
	def __init__(self):	
		self.head = None ## root node
		self.size = 0

	def insertstart(self, data):	## O(1) -- very fast
		self.size += 1
		newnode = node(data)

		if not self.head:
			self.head = newnode
		else:
			newnode.nextnode = self.head
			self.head = newnode

	def remove(self, data):
		if self.head is None:
			return 

		prevnode = None
		currentnode = self.head
		
		while currentnode.data != data:
			prevnode = currentnode
			currentnode = currentnode.nextnode

		
		if prevnode is not None: 		
			prevnode.nextnode = currentnode.nextnode

		else:
			self.head = currentnode.nextnode
		
		self.size -= 1 

	def size1(self): ## O(1) very fast
		return self.size

	def size_(self): ## O(N) 
		actualnode = self.head
		size = 0
		
		while actualnode is not None:
			self.size += 1	
			actualnode = actualnode.nextnode
		
		return size

	def insertend(self, data): ## O(N)		
		self.size += 1
		newnode = node(data)
		actualnode = self.head

		while actualnode.nextnode is not None:
			actualnode = actualnode.nextnode
				
		actualnode.nextnode = newnode

	def traversing(self):
		actualnode = self.head

		while actualnode is not None:
			print("%d "%actualnode.data)
			actualnode = actualnode.nextnode

ll = linked_list()
ll.insertstart(12)
ll.insertstart(4)
ll.insertstart(545)
ll.insertend(15)
ll.traversing()

ll.remove(12)
ll.remove(545)

print(ll.size1())




