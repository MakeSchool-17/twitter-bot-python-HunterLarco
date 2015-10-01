import sys
import timeit
import random

import HistogramByMap
import HistogramByTrieTree
import HistogramByTupleArray



if __name__ == '__main__':
  iterations = 50000
  word_range = range(1000)
  
  print('\n')
  print('---------------------')
  print('Test Started')
  print('Iterations: '+str(iterations))
  print('---------------------')
  
  dictionary = open('/usr/share/dict/words').read().split('\n')
  hist1 = HistogramByMap.Histogram(dictionary[word_range[0]:word_range[-1]])
  hist2 = HistogramByTrieTree.Histogram(dictionary[word_range[0]:word_range[-1]])
  hist3 = HistogramByTupleArray.Histogram(dictionary[word_range[0]:word_range[-1]])
   
  hists = [
    (hist1, 'Map'),
    (hist2, 'TrieTree'),
    (hist3, 'Tuple Array')
  ]
  
  words = [
    (dictionary[random.choice(word_range)], 'Word In Histogram'),
    ('notaword', 'Word Not In Histogram')
  ]
  
  for word,title in words:
    print(title)
    
    for hist,name in hists:
      totaltime = 0

      stmt  = "hist.getFrequency(word)"
      setup = "from __main__ import hist, word"
      timer = timeit.Timer(stmt, setup=setup)
      result = timer.timeit(number=iterations)
    
      print(name+': '+str(result))
      
    print('---------------------')
  
  print('Test Ended')
  print('---------------------')
  print('\n')