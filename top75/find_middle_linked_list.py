# 23. How to find the middle element of a singly linked list in one pass?


class ErrorCycle(Exception):
	def __init__(self):
		print("Cycle Detected")

class Link:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		temp = Link(data)
		if not self.head:
			self.head = temp
		else:
			current = self.head
			while current.next != None:
				current = current.next
			current.next = temp

	def print(self):
		pointer = self.head

		if self.detect_cycle():
			raise ErrorCycle

		while pointer != None:
			print(pointer.data)
			pointer = pointer.next


	def middle_element(self):
		'''
		Detect middle element in one pass
		'''
		once = self.head
		twice = self.head

		if self.detect_cycle():
			raise ErrorCycle

		while twice.next != None:
			once = once.next
			twice = twice.next
			if twice != None and twice.next != None :
				twice = twice.next

		return once.data

	def length(self):
		llength = 1
		current = self.head

		while current.next != None:
			current = current.next
			llength+=1

		return llength



	def create_cycle(self):
		temp = self.head
		i = 0
		while i > 2 and temp.next != None:
			print("here", temp.data)
			temp = temp.next
			i+=1

		temp.next = self.head

	def detect_cycle(self):
		pointer = self.head

		storage = set()

		while pointer != None:
			if pointer in storage:
				print("Cycle", pointer.data)
				return True
			storage.add(pointer)
			pointer=pointer.next

		return False


		# pointer1 = self.head
		# pointer2 = self.head

		# addresses = set()		
		# while pointer2 != None and pointer2.next != None:

		# 	pointer1 = pointer1.next
		# 	pointer2 = pointer2.next.next

		# 	if pointer1 == pointer2:
		# 		print("Cycle", pointer2.data)
		# 		return True

		# return False




a = LinkedList()
a.insert(2)
a.insert(13)
a.insert(12)
a.insert(3)
a.insert(14)
a.insert(15)
a.insert(1)

print(a.length())

a.print()
print()
a.create_cycle()
# print(a.middle_element())
a.print()
print(a.detect_cycle())

