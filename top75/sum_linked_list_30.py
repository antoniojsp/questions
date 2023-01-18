# sum
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
		"""
		Value is saved from right to left.
		"""
		current = self.head
		result = []
		while current:
			result.append(str(current.data))
			current = current.next

		print("".join(result[::-1]))

	def len(self):
		return self.length

	def sum(self, head):

		first = self.head
		second = head.head
		stack = []
		sumation = LinkedList()
		reminder = 0
		while first or second:
			if first:
				reminder += first.data
				first = first.next
			if second:
				reminder += second.data
				second = second.next

			if reminder > 9:
				sumation.insert(reminder % 10)
				reminder = 1
			else:
				sumation.insert(reminder)
				reminder = 0

		return sumation


def titles(name, repeat):
	design = "#" * repeat
	print(design, name, design)

titles("Values",10)
a = LinkedList()
# add from right to left i.e inserting 1, 2,3,3 gives us 3321
a.insert(9)
a.insert(2)
a.insert(3)
a.insert(1)
a.insert(1)
a.insert(1)

a.print()

b = LinkedList()
b.insert(1)
b.insert(1)
# b.insert(9)

b.print()
titles("Suma", 10)
result = a.sum(b)
nuevo = result.sum(b)
nuevo.print()

