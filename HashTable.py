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
    self.bins = [LinkedList() for i in range(0,prime)]
    
    print('grow: '+str(len(self.bins)))
    
    for key, value in items:
      self.set(key, value)
  
  
  def __init__(self, bins=101):
    self.bins = [LinkedList() for i in range(0,bins)]
    self.size = 0
  
  def set(self, key, value):
    if self.size / len(self.bins) > 0.7:
      self.__grow__()
    
    entry = self.get(key, tuple=True)
    if not entry:
      self.size += 1
      binindex = hash(key) % len(self.bins)
      self.bins[binindex].add([key, value])
    else:
      entry[1] = value
  
  def get(self, key, tuple=False):
    binindex = hash(key) % len(self.bins)
    linkedlist = self.bins[binindex]
    query = linkedlist.find(lambda x: x[0] == key)
    return None if len(query) == 0 else (query if tuple else query[1])
  
  def remove(self, key):
    binindex = hash(key) % len(self.bins)
    linkedlist = self.bins[binindex]
    linkedlist.delete(key, expression=lambda a,b: a[0] == b)
    self.size -= 1
  
  def keys(self):
    keys = []
    for linkedlist in self.bins:
      for item in linkedlist:
        keys.append(item[0])
    return keys
  
  def values(self):
    values = []
    for linkedlist in self.bins:
      for item in linkedlist:
        values.append(item[1])
    return values
  
  def items(self):
    items = []
    for linkedlist in self.bins:
      for item in linkedlist:
        items.append(item)
    return items
    


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
    print(table.bins[i].toString())

