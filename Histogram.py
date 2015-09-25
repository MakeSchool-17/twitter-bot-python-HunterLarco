import sys
import random


class Histogram:
  
  # O(n) if given array
  # O(2n) if given text
  def __init__(self, arg):
    self.__FormFromArray__(arg) if isinstance(arg, list) else self.__FormFromText__(arg)
  
  # O(n)
  def __FormFromText__(self, text):
    self.__FormFromArray__(text.split(' '))
  
  # O(n)
  def __FormFromArray__(self, words):
    histogram = {}
    for word in words:
      histogram[word] = 1 if not word in histogram else histogram[word]+1
    self.structure = histogram
    self.words     = words
  
  # O(1)
  def getUniqueWords(self):
    return self.structure.keys()
  
  # O(1)
  def getFrequency(self, word):
    return self.structure[word] if word in self.structure else 0



if __name__ == '__main__':
  text = open('/Users/hunterlarco/Documents/Github Repos/twitter-bot-python-HunterLarco/endersgame.txt', 'r').read()
  hist = Histogram(text.split(' '))
  
  print(hist)
  print(hist.getFrequency('I'))
  print(hist.getFrequency('Ender'))
  print(hist.getFrequency('I\'ll'))
