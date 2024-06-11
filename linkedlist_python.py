class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None

   def listprint(self):
      printval = self.head
      while printval is not None:
         print (printval.data)
         printval = printval.next

list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4=Node("Thu")

# Link first Node to second node
list.head.next = e2

# Link second Node to third node
e2.next = e3
e3.next=e4

list.listprint()