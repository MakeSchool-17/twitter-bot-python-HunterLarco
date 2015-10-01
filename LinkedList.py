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
  
  def get(self, index, wrap=True):
    if wrap: index = index % len(self)
    for i, value in enumerate(self):
      if i == index:
        return value
    return None
  
  def head(self):
    return self.head
  
  def tail(self):
    return self.head.left
  
  def find(self, expression, findall=False):
    if findall:
      return [value for value in self if expression(value)]
    else:
      for value in self:
        if expression(value):
          return value
      return None
  
  def delete(self, value, expression = lambda a,b: a == b):
    if len(self) == 1:
      self.head = None
      self.size = 0
      return True
    
    for node in self.__iter__(return_nodes=True):
      if expression(node.value, value):
        if node == self.head:
          self.head = node.right
        
        node.left.right = node.right
        node.right.left = node.left
        
        self.size -= 1
        return True;
    
    return False
  
  def __iter__(self, return_nodes=False):
    return LinkedListIterator(self.head, return_nodes=return_nodes)
  
  def __str__(self):
    return '['+', '.join([str(item) for item in self])+']'
  
  def __len__(self):
    return self.size





class LinkedListIterator:
  
  def __init__(self, head, return_nodes=False):
    self.head = head
    self.node = head
    self.firstpass = True
    self.return_nodes = return_nodes
  
  def __iter__(self):
    return self
  
  def next(self):
    return self.__next__()
  def __next__(self):
    if self.head and (self.node != self.head or self.firstpass == True):
      self.firstpass = False
      node = self.node
      self.node = node.right
      return node if self.return_nodes else node.value
    else:
      raise StopIteration




class LinkedListNode:
  
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left  = None

  def __str__(self):
    return str(self.value)



if __name__ == '__main__':
  linkedlist = LinkedList()
  
  linkedlist.add(6)
  linkedlist.add(3)
  linkedlist.add(5)
  linkedlist.add(4)
  
  print(linkedlist)
  
  print(linkedlist.get(0))# 6
  print(linkedlist.get(1))# 3
  print(linkedlist.get(2))# 5
  print(linkedlist.get(3))# 4
  print(linkedlist.get(4))# 6
  print(linkedlist.get(4, wrap=None))# None
  print(linkedlist.get(-2))# 5
  
  print('Find x>3: '+str(linkedlist.find(lambda x: x > 3)))
  print('Find x>3 findall: '+str(linkedlist.find(lambda x: x > 3, findall=True)))
  
  linkedlist.delete(5)
  
  print(linkedlist)
  
  linkedlist = LinkedList(arr=[1,2,3])
  print('1: '+str(linkedlist))
  linkedlist.delete(3)
  print('2: '+str(linkedlist))
  linkedlist.delete(1)
  print('3: '+str(linkedlist))
  linkedlist.delete(2)
  print('4: '+str(linkedlist))

