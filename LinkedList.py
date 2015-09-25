class LinkedList:
  
  def __init__(self, arr=[]):
    self.head = None
    self.size = 0
    for item in arr:
      self.add(item)
  
  def add(self, value):
    newnode = LinkedListNode(value)
    self.size += 1
    
    if not self.head:
      newnode.left = newnode
      newnode.right = newnode
      self.head = newnode
      return
    
    self.insertAfter(self.tail(), newnode)
  
  def insertBefore(self, node, newnode):
    newnode.right = node
    newnode.left = node.left
    node.left.right = newnode
    node.left = newnode
    if node == self.head:
      self.head = newnode
  
  def insertAfter(self, node, newnode):
    node.right.left = newnode
    newnode.right = node.right
    node.right = newnode
    newnode.left = node
  
  def get(self, index):
    index = index % self.length()
    node = self.head
    i = 0
    while i < index:
      node = node.right
      i += 1
    return node.value
  
  def length(self):
    return self.size
  
  def head(self):
    return self.head
  
  def tail(self):
    return self.head.left
  
  def find(self, expression, findall=False):
    output = []
    
    node = self.head
    firstpass = True
    while self.head and (node != self.head or firstpass == True):
      firstpass = False
      if expression(node.value):
        if findall: output.append(node.value)
        else: return node.value
      node = node.right
    
    return output
  
  def delete(self, value, expression = lambda a,b: a == b):
    if self.length() == 1:
      self.head = None
      return
    
    node = self.head
    firstpass = True
    while self.head and (node != self.head or firstpass == True):
      firstpass = False
      if expression(node.value, value):
        self.size -= 1
        
        if node == self.head:
          self.head = node.right
        
        node.left.right = node.right
        node.right.left = node.left
        return True
      node = node.right
      
    return False
  
  def toString(self):
    string = ''
    node = self.head
    firstpass = True
    while self.head and (node != self.head or firstpass == True):
      firstpass = False
      string += str(node.value)+', '
      node = node.right
    return '['+string[:-2]+']'
  
  def __iter__(self):
    return LinkedListIterator(self.head)





class LinkedListIterator:
  
  def __init__(self, head):
    self.head = head
    self.node = head
    self.firstpass = True
  
  def __iter__(self):
    return self
  
  def next(self):
    return self.__next__()
  def __next__(self):
    if self.head and (self.node != self.head or self.firstpass == True):
      self.firstpass = False
      node = self.node
      self.node = node.right
      return node.value
    else:
      raise StopIteration




class LinkedListNode:
  
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left  = None



if __name__ == '__main__':
  linkedlist = LinkedList()
  
  linkedlist.add(6)
  linkedlist.add(3)
  linkedlist.add(5)
  linkedlist.add(4)
  
  print(linkedlist.toString())
  
  print(linkedlist.get(0))# 6
  print(linkedlist.get(1))# 3
  print(linkedlist.get(2))# 5
  print(linkedlist.get(3))# 4
  print(linkedlist.get(4))# 6
  print(linkedlist.get(-2))# 5
  
  print(linkedlist.find(lambda x: x > 3))
  print(linkedlist.find(lambda x: x > 3, findall=True))
  
  linkedlist.delete(5)
  
  print(linkedlist.toString())
  
  linkedlist = LinkedList(arr=[1,2,3])
  print('1: '+linkedlist.toString())
  linkedlist.delete(3)
  print('2: '+linkedlist.toString())
  linkedlist.delete(1)
  print('3: '+linkedlist.toString())
  linkedlist.delete(2)
  print('4: '+linkedlist.toString())

