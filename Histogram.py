import sys
import random
from HashTable import HashTable


class Histogram:
  
  # O(n) if given array
  # O(2n) -> O(n) if given text
  def __init__(self, arg):
    self.__FormFromArray__(arg) if isinstance(arg, list) else self.__FormFromText__(arg)
  
  # O(n)
  def __FormFromText__(self, text):
    self.__FormFromArray__(text.split(' '))
  
  # O(n)
  def __FormFromArray__(self, words):
    histogram = HashTable()
    for word in words:
      histogram.set(word, histogram.get(word)+1) if histogram.has(word) else histogram.set(word, 1)
    self.structure = histogram
    self.words     = words
  
  # O(n)
  def getUniqueWords(self):
    return self.structure.keys()
  
  def getTotalWords(self):
    return self.words
  
  # O(n)
  def getFrequency(self, word):
    freq = self.structure.get(word)
    return freq if freq else 0
  
  
  def __str__(self):
    return str(self.structure)
  



if __name__ == '__main__':
  text = open('endersgame.txt', 'r').read()
  hist = Histogram(text.split(' '))
  
  print(hist)
  print(hist.getFrequency('I'))
  print(hist.getFrequency('Ender'))
  print(hist.getFrequency('I\'ll'))
  print(len(hist.getUniqueWords()))
  print(len(hist.getTotalWords()))
