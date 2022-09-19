# 25. How to reverse a linked list? (solution)

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
			pointer = self.head
			while pointer.next != None:
				pointer = pointer.next
			pointer.next = temp

	def print(self):
		pointer = self.head

		while pointer != None:
			print(pointer.data)
			pointer = pointer.next

	def reverse(self):

		'''
		three pointers: pointer set as start of the link, and next_link and prev set as None

		loop through the limked list

		storage the next link from the current link

		set the current link "next" as the previos attr (Starts with None)

		set prev as the current link (we will set the next link "next" attr as prev)

		finally, rotate the loop by setting the pointer as the next_link (which we storage previoslu before changing it)

		'''

		pointer = self.head #current link to review
		next_link = None # storage the next link before editing the pointer
		prev = None # save the previos pointer that would be set as next pointer to the next link.

		while pointer != None:
			next_link = pointer.next
			pointer.next = prev
			prev = pointer
			pointer = next_link

		self.head = prev # set head as prev since contains the last link processed.










a = LinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)
print("LIST")
a.print()

a.reverse()
print("REVERSED")
a.print()


