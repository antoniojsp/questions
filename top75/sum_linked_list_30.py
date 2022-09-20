# 23. How to find the middle element of a singly linked list in one pass?


class ErrorCycle(Exception):
	def __init__(self):
		print("Cycle Detected")

class ErrorLength(Exception):
	def __init__(self):
		print("Location out of bounds")



class Link:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.length = 0

	def insert(self, data):
		insert = Link(data)
		if not self.head:
			self.head = insert
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = insert

		self.length +=1

	def print(self):
		current = self.head
		while current:
			print(current.data, end="")
			current = current.next

		print()

	def len(self):
		return self.length

	def sum(self, head):

		current = self.head
		stack1 = []
		while current:
			stack1.append(current.data)
			current =  current.next
		
		current2 = head.head
		stack2 = []
		while current2:
			stack2.append(current2.data)
			current2 =  current2.next

		# i = 0
		# suma = 0	
		# carry = 
		# while stack1 or stack2:
		# 	a = 0
		# 	b = 0
		# 	if stack1:
		# 		a = stack1.pop()
		# 	if stack2:
		# 		b = stack2.pop()

		# 	if a + b > 9:
		# 		suma += ((a+b)-10)*10**i
			

		# 	i+=1

		# print(suma)

		current = self.head
		stack1 = []
		while current:
			stack1.append(current.data)
			current =  current.next
		
		current2 = head.head
		stack2 = []
		while current2:
			stack2.append(current2.data)
			current2 =  current2.next

		suma = 0
		for i in range(0,len(stack1)):
			temp = stack1.pop()
			suma += temp*(10**i)

		for i in range(0,len(stack2)):
			temp = stack2.pop()
			suma += temp*(10**i)

		return suma

		


def p(val):
	print("#####",val,"#####")

a = LinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(3)

a.print()

b = LinkedList()
b.insert(3)
b.insert(2)
b.insert(1)

b.print()
p("Suma")
print(a.sum(b))


