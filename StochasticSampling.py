import sys
import random
import Histogram


def quasirandom(histogram):
  return random.choice(Histogram.unique_words(histogram))


def weightedrandom(histogram):
  return random.choice(histogram['meta']['words'])


if __name__ == '__main__':
  hist = Histogram.histogram('hunter is the coolest hunter, right hunter?')
  print(quasirandom(hist))
  print(weightedrandom(hist))
  
  arr = []
  for i in range(10000):
    arr.append(weightedrandom(hist))
  
  print Histogram.histogram_from_array(arr)