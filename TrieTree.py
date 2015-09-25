class TrieTree:
  
  # O(Mn) where M is item length and n the amount of items
  def __init__(self, arr=[]):
    self.head = {'letters':{}, 'isend':False, 'data':None}
    for item in arr:
      if isinstance(item, tuple): self.add(item[0], data=item[1])
      else: self.add(item)
  
  # O(M) where M is item length
  def add(self, item, data=None):
    self.__add__(self.head, item, data=data)
  
  # O(M) where M is item length
  def __add__(self, node, item, data=None):
    if len(item) == 0:
      node['isend'] = True
      node['data']  = data
      return
    
    letter = item[0]
    if not letter in node['letters']:
      node['letters'][letter] = {'letters':{}, 'isend':False, 'data':None}
    
    self.__add__(node['letters'][letter], item[1:], data=data)
  
  # O(M) where M is amount of letters from all words
  # larger than O(n) where n is the amount of words
  def items(self):
    return self.__items__(self.head, '')
  
  # O(M) where M is amount of letters from all words
  # larger than O(n) where n is the amount of words
  def __items__(self, node, value):
    items = [value] if node['isend'] else []
    for letter,node in node['letters'].items():
      items += self.__items__(node, value+letter)
    return items
  
  # O(M) where M is item length
  def get(self, item):
    return self.__get__(self.head, item)
  
  # O(M) where M is item length
  def __get__(self, node, item):
    if len(item) == 0:
      return {'data': node['data']} if node['isend'] else None
    
    letter = item[0]
    if not letter in node['letters']:
      return None
    
    return self.__get__(node['letters'][letter], item[1:])



if __name__ == '__main__':
  tree = TrieTree([('hunter', 'test'), 'hunted', 'hunt', 'hunts', 'hunger', 'who'])
  
  import json
  print(json.dumps(tree.head, indent=2, sort_keys=True))
  
  print(tree.get('hunters'))
  print(tree.get('hunts'))
  print(tree.get('hunter'))
  
  print(tree.items())
