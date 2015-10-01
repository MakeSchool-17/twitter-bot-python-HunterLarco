class Histogram:
  
  # O(n) if given array
  # O(2n) -> O(n) if given text
  def __init__(self, arg):
    self.__FormFromArray__(arg) if isinstance(arg, list) else self.__FormFromText__(arg)
  
  # O(n)
  def __FormFromArray__(self, words):
    histogram = {}
    for word in words:
      histogram[word] = 1 if not word in histogram else histogram[word]+1
    self.structure = histogram
    self.words     = words
  
  # O(n)
  def __FormFromText__(self, text):
    import re
    stripped = re.sub('[^a-zA-Z\s]', '', text)
    words = stripped.split(' ')
    return self.__FormFromArray__(words)

  # O(1)
  def getUniqueWords(self):
    return self.structure.keys()
  
  # O(1)
  def getFrequency(self, word):
    return self.structure[word] if word in self.structure else 0



if __name__ == '__main__':
  hist = Histogram('hunter is the coolest hunter')
  
  print(hist)
  print(hist.getUniqueWords())
  print(hist.getFrequency('hunter'))
  print(hist.getFrequency('is'))