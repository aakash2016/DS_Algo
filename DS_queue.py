## Day 2
## QUEUE <<- implementation using arrays. 
class queue:
	def __init__(self):
		self.queue = []
	
	def isempty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def size(self):
		return len(self.queue)

q = queue()
q.enqueue(112)
q.enqueue(5)
q.enqueue(10)
print("Dequeued ", q.dequeue())
print(q.size())
print("peek", q.peek())
