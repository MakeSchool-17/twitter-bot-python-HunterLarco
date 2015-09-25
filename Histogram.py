import sys
import random


def histogram(text):
  import re
  stripped = re.sub('[^a-zA-Z\s]', '', text)
  words = stripped.split(' ')
  return histogram_from_array(words)

def histogram_from_array(words):
  histogram = {'meta': {'words': words}, 'histogram': {}}
  for word in words:
    histogram['histogram'][word] = 1 if not word in histogram['histogram'] else histogram['histogram'][word]+1
  return histogram


def unique_words(histogram):
  return histogram['histogram'].keys()


def frequency(word, histogram):
  return histogram['histogram'][word]


if __name__ == '__main__':
  hist = histogram('hunter is the coolest hunter')
  words = unique_words(hist)
  freq = frequency('hunter', hist)
  
  print(hist)
  print(words)
  print(freq)