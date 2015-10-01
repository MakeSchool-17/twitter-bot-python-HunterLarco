import sys
import random

def rearrange(arr):
  copy = arr[:]
  random.shuffle(copy)
  return copy

if __name__ == '__main__':
  arr = sys.argv[1:] if len(sys.argv) > 1 else ['one','two','three','four','five']
  words = rearrange(arr)
  print(words)