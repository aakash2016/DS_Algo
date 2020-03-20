## Day 2
## STACK <<- implementation using arrays. 
class stack:
	def __init__(self):
		self.stack = []

	def isempty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1] ## delete the reference.
		return data 
	
	def peek(self):
		return self.stack[-1]

	def size(self):
		return len(self.stack)

stac = stack()
stac.push(1)
stac.push(51)
stac.push(5)
stac.push(4)

print("popped", stac.pop())
print("peek", stac.peek())
print(stac.size())
