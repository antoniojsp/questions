class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

class Tree:

	def __init__(self):
		self.root = None

	def insert(self, data):
		new_node = Node(data)

		if self.root == None:
			self.root = new_node
		else:
			current = self.root

			while current:
				if 