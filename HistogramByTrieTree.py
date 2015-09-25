import sys
import random
import TrieTree


class Histogram:
  
  def __init__(self, arg):
    self.__FormFromArray__(arg) if isinstance(arg, list) else self.__FormFromText__(arg)
  
  # O(Mn)
  def __FormFromArray__(self, words):
    self.structure = TrieTree.TrieTree()
    
    for word in words:
      node = self.structure.get(word)
      if node: self.structure.add(word, data=node['data']+1)
      else: self.structure.add(word, data=1)
  
  # O(Mn)
  def __FormFromText__(self, text):
    import re
    stripped = re.sub('[^a-zA-Z\s]', '', text)
    words = stripped.split(' ')
    return self.__FormFromArray__(words)

  # O(M) where M is total nodes
  def getUniqueWords(self):
    return self.structure.items()
  
  # O(M) where M is item length
  def getFrequency(self, word):
    item = self.structure.get(word)
    return item['data'] if item else 0



if __name__ == '__main__':
  hist = Histogram('hunter is the coolest hunter')
  
  print(hist)
  print(hist.getUniqueWords())
  print(hist.getFrequency('hunter'))
  print(hist.getFrequency('is'))