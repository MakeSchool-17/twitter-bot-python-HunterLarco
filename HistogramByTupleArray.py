class Histogram:
  
  def __init__(self, arg):
    self.__FormFromArray__(arg) if isinstance(arg, list) else self.__FormFromText__(arg)
  
  # O(n^2)
  def __FormFromArray__(self, words):
    array = []
    
    for word in words:
      index = None
      for i, (tupword, count) in enumerate(array):
        if tupword == word:
          index = i
          break
      
      if index != None:
        tup = array[index]
        array[index] = (tup[0], tup[1]+1)
      else:
        array.append((word, 1))
      
    self.structure = array
    self.words     = words
  
  # O(n^2+n) -> O(n^2)
  def __FormFromText__(self, text):
    import re
    stripped = re.sub('[^a-zA-Z\s]', '', text)
    words = stripped.split(' ')
    return self.__FormFromArray__(words)

  # O(n)
  def getFrequency(self, word):
    for tupword, count in self.structure:
      if tupword == word:
        return count
    return 0



if __name__ == '__main__':
  hist = Histogram('hunter is the coolest hunter')
  
  print(hist.structure)
  print(hist.getFrequency('hunter'))
  print(hist.getFrequency('is'))