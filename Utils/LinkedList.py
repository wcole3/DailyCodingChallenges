"""
Simple singly linked list implementation.
"""
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def print_list(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

   def add_node(self, data):
      new_node = Node(data)
      new_node.nextval = self.headval
      self.headval = new_node

   def create_list(self, data):
      self.headval = None
      for d in data:
         self.add_node(d)

   def size(self):
      count = 0
      current = self.headval
      while current is not None:
         count += 1
         current = current.nextval
      return count



