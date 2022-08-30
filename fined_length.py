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
         print(temp.dataval, end=" ")
         temp = temp.nextval
      print()

   def find_middle(self):
      once = self.headval
      twice = self.headval

      while twice.nextval != None:
         twice = twice.nextval
         if twice != None and twice.nextval != None:
            once = once.nextval
            twice = twice.nextval

      return once.dataval

   def reverse(self):
      prev =  None
      current = self.headval
      next = None

      while  current != None:
         next = current.nextval # save the adddress for the next node to keep track what node is visiting
         current.nextval = prev # set next value to previous (going backwards)
         prev = current # set previous as current 
         current = next # move current as next to use the next node
      self.headval = prev # set previous as head

   def remove_duplicate(self):

      duplicate = {}
      current = self.headval
      prev = None
      while current != None:
         current_value = current.dataval
         if current_value in duplicate:
            duplicate[current_value] += 1
            prev.nextval = current.nextval
            current = prev.nextval
            continue
         else:
            duplicate[current_value] = 1

         prev = current
         current = current.nextval
         
   def length(self):
      count = 0
      current = self.headval

      while current != None:
         count +=1
         current = current.nextval

      return count


      


list1 = SLinkedList()
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(4)
list1.insert(6)
list1.insert(6)
list1.insert(6)
list1.insert(6)
list1.insert(6)
list1.insert(4)
list1.insert(4)
list1.insert(4)
list1.insert(6)
list1.insert(5)
list1.insert(5)
list1.insert(5)
list1.insert(6)
list1.insert(6)
list1.insert(6)
list1.insert(6)
print(list1.length())

list1.print()
