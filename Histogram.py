import sys
import random


def histogram(text):
  import re
  stripped = re.sub('[^a-zA-Z\s]', '', text)
  words = stripped.split(' ')
  
  histogram = {}
  for word in words:
    histogram[word] = 1 if not word in histogram else histogram[word]+1
  
  return histogram


def unique_words(histogram):
  return histogram.keys()


def frequency(word, histogram):
  return histogram[word]


if __name__ == '__main__':
  hist = histogram('hunter is the coolest hunter')
  words = unique_words(hist)
  freq = frequency('hunter', hist)
  
  print(hist)
  print(words)
  print(freq)