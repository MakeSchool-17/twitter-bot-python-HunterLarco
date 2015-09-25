import sys
import random
import Histogram


def quasirandom(histogram):
  return random.choice(histogram.getUniqueWords())


def weightedrandom(histogram):
  return random.choice(histogram.words)


if __name__ == '__main__':
  hist = Histogram.Histogram('hunter did this and that so hunter is a hunter')
  print(quasirandom(hist))
  print(weightedrandom(hist))
  
  arr = []
  for i in range(10000):
    arr.append(weightedrandom(hist))
  
  print Histogram.Histogram(arr).structure