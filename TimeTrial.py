import sys
import timeit

import HistogramByMap
import HistogramByTrieTree
import HistogramByTupleArray



if __name__ == '__main__':
  iterations = 50000
  
  print('\n')
  print('---------------------')
  print('Test Started')
  print('Iterations: '+str(iterations))
  print('---------------------')
  
  dictionary = open('/usr/share/dict/words').read().split('\n')
  hist1 = HistogramByMap.Histogram(dictionary[:1000])
  hist2 = HistogramByTrieTree.Histogram(dictionary[:1000])
  hist3 = HistogramByTupleArray.Histogram(dictionary[:1000])
   
  hists = [
    (hist1, 'Map'),
    (hist2, 'TrieTree'),
    (hist3, 'Tuple Array')
  ]
  
  words = [
    (dictionary[100], 'Word In Histogram'),
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