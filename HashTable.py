from LinkedList import LinkedList


class HashTable:
  
  @classmethod
  def genPrime(cls, seed=0):
    seed += 1
    while not cls.isPrime(seed):
      seed += 1
    return seed
  
  @classmethod
  def isPrime(cls, num):
    for i in range(2,num):
      if num % i == 0:
        return False
    return True
  
  @classmethod
  def doublePrime(cls, prime):
    return cls.genPrime(seed=prime*2)
  
  
  def __grow__(self):
    items = self.items()
    
    prime = self.doublePrime(len(self.bins))
    self.bins = [None] * prime
    
    # print('grow: '+str(len(self.bins)))
    
    for key, value in items:
      self.set(key, value)
  
  
  def __init__(self, bins=101):
    bins = self.genPrime(seed=bins)
    self.originalbins = bins
    self.bins = [None] * bins
    self.size = 0
  
  def clone(self):
    table = self.__class__(bins=len(self.bins))
    for key, value in self:
      table.set(key, value)
    return table
  
  def reset(self):
    self.size = 0
    self.bins = [None] * self.originalbins
  
  def clear(self):
    self.size = 0
    self.bins = [None] * len(self.bins)
  
  def has(self, key):
    return self.get(key) != None
  
  def set(self, key, value):
    if self.size / len(self.bins) > 0.7:
      self.__grow__()
    
    entry = self.get(key, return_tuple=True)
    if not entry:
      self.size += 1
      binindex = hash(key) % len(self.bins)
      if not self.bins[binindex]:
        self.bins[binindex] = LinkedList()
      self.bins[binindex].add([key, value])
    else:
      entry[1] = value
  
  def get(self, key, return_tuple=False):
    binindex = hash(key) % len(self.bins)
    linkedlist = self.bins[binindex]
    if linkedlist == None:
      return None
    query = linkedlist.find(lambda x: x[0] == key)
    if query == None:
      return None
    return query if return_tuple else query[1]
  
  def remove(self, key):
    binindex = hash(key) % len(self.bins)
    linkedlist = self.bins[binindex]
    linkedlist.delete(key, expression=lambda a,b: a[0] == b)
    if len(linkedlist) == 0:
      self.bins[binindex] = None
    self.size -= 1
  
  def keys(self):
    keys = []
    for linkedlist in self.bins:
      if linkedlist:
        for item in linkedlist:
          keys.append(item[0])
    return keys
  
  def values(self):
    values = []
    for linkedlist in self.bins:
      if linkedlist:
        for item in linkedlist:
          values.append(item[1])
    return values
  
  def items(self):
    items = []
    for linkedlist in self.bins:
      if linkedlist:
        for item in linkedlist:
          items.append(item)
    return items
  
  def __iter__(self):
    return HashTableIterator(self.bins)
  
  def __len__(self):
    return self.size
  
  def __str__(self, pretty_print=False):
    if pretty_print:
      return '{\n  '+',\n  '.join(['\''+str(key)+'\': '+str(value) for key, value in self])+'\n}'
    else:
      return '{'+', '.join(['\''+str(key)+'\': '+str(value) for key, value in self])+'}'




class HashTableIterator:
  
  def __init__(self, bins):
    self.bins = bins
    self.binindex = 0
    self.listindex = 0
  
  def __iter__(self):
    return self
  
  def next(self):
    return self.__next__()
  def __next__(self):
    while(True):
      if self.binindex < len(self.bins):
        linkedlist = self.bins[self.binindex]
        if linkedlist and self.listindex < len(linkedlist):
          update = linkedlist.get(self.listindex)
          self.listindex += 1
          return update
        else:
          self.binindex += 1
          self.listindex = 0
      else:
        raise StopIteration

    


if __name__ == '__main__':
  table = HashTable(bins=101)

  table.set('hello', 'world')
  print(table.get('hello'))
  print(table.keys())
  print(table.values())

  table.set('hello', 'you')
  print(table.get('hello'))
  print(table.keys())
  print(table.values())

  table.set('hello', 'hunter')
  table.set('how', 'are')
  table.set('you', '?')

  print(table.keys())
  print(table.values())

  print(table.get('you'))

  table.set((1,2,3), 'array')
  print(table.keys())
  print(table.get((1,2,3)))

  table.remove('hello')
  print(table.keys())
  print(table.values())

  for i in range(1000):
    table.set(i, i);

  for i in range(80,120):
    print(table.bins[i])

  table.clear()
  
  for i in range(100):
    table.set(i, i);
  for (item, value) in table:
    print(str(item)+': '+str(value))
  
  table2 = table.clone()
  table2.clear()
  
  print(table.get(0))
  print(table2.get(0))
  
  print(table)
  print(table2)
  
  table = HashTable()
  table.set('Hunter', 18)
  table.set('John', 4)
  table.set('Emily', 19)
  table.set('Ruth', 11)
  print(table.__str__(pretty_print=True))

