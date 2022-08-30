class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def insert(self, data):
      new_node = Node(data)

      if not self.headval:
         self.headval = new_node
      else:
         temp = self.headval
         while temp.nextval != None:
            temp = temp.nextval
         temp.nextval = new_node

   def print(self):
      temp = self.headval
      while temp != None:
         print(temp.dataval)
         temp = temp.nextval

   def find_middle(self):
      once = self.headval
      twice = self.headval

      while twice.nextval != None:
         twice = twice.nextval
         if twice != None and twice.nextval != None:
            once = once.nextval
            twice = twice.nextval

      print(once.dataval)


list1 = SLinkedList()
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)
list1.insert(6)
list1.insert(6)


list1.find_middle()


