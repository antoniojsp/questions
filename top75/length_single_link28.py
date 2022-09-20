# 28. How to find the length of a singly linked list? (solution)


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

	def insert(self, data):
		insert = Link(data)
		if not self.head:
			self.head = insert
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = insert

	def print(self):
		current = self.head

		if self.detect_cycle():
			raise ErrorCycle

		while current:
			print(current.data)
			current = current.next


	def middle_element(self):
		'''
		Detect middle element in one pass
		'''
		one_step = self.head
		two_steps = self.head

		if self.detect_cycle():
			raise ErrorCycle

		while two_steps.next:
			one_step = one_step.next
			two_steps = two_steps.next
			if two_steps and two_steps.next:
				two_steps = two_steps.next

		return once.data

	def length(self):
		llength = 1
		current = self.head

		while current.next:
			current = current.next
			llength+=1

		return llength

	#recursive
	def length_recursive(self, node):
		if node == None:
			return 0

		return 1 + self.length_recursive(node.next)

	def length_rec(self):
		return self.length_recursive(self.head)


	def create_cycle(self, location):

		if location >= self.length():
			raise ErrorLength

		current = self.head
		while current.next:
			current = current.next

		i = 0
		index = self.head
		while i < location:
			index = index.next
			i+=1
		print("Cycle created in", index.data)
		current.next = index

	def detect_cycle(self):
		'''
		using set
		'''
		# pointer = self.head
		# storage = set()
		# while pointer:
		# 	if pointer in storage:
		# 		print("Cycle in (detected)", pointer.data)
		# 		return True
		# 	storage.add(pointer)
		# 	pointer=pointer.next

		# return False

		'''
		Detects loop but cannot detect location. Use set instead
		'''
		pointer1 = self.head
		pointer2 = self.head
		while pointer2 and pointer2.next:
			pointer1 = pointer1.next
			pointer2 = pointer2.next.next
			if pointer1 == pointer2:
				return True
		return False


	def remove_duplicate(self):
		duplicate = {}
		current = self.head
		prev = None
		while current:
			if current.data in duplicate:
				prev.next = current.next
			else:
				duplicate[current.data] = True
				prev = current

			current = current.next

	def thirdNodeEnd(self):

		'''

		With Data Structure
		'''
		# positions = []
		# current = self.head
		# while current:
		# 	positions.append(current.data)
		# 	current = current.next
		# return positions[-3]


		result = self.head
		top_stop = self.head

		i = 0

		while top_stop:

			top_stop = top_stop.next
			if i > 2:
				result = result.next
			i +=1


		# for times in range(3):
		# 	top_stop = top_stop.next

		# while top_stop:
		# 	result = result.next
		# 	top_stop = top_stop.next

		# while top_stop:


		return result.data

def p(val):
	print("\n#####",val,"#####\n")


a = LinkedList()
a.insert(47)
a.insert(2)
a.insert(34)
a.insert(47)
a.insert(2)
a.insert(34)
a.insert(47)
print("third", a.thirdNodeEnd())

# p("Original")
# a.print()
# print("Length:", a.length_rec())
# a.remove_duplicate()
# p("Remove duplicates")
# a.print()

# print("Length:", a.length_rec())

