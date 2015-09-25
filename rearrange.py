import sys
import random

def rearrange(arr):
  # return [arr.pop(random.randint(0, len(arr)-1)) for i in range(len(arr))]
  copy = arr[:]
  random.shuffle(copy)
  return copy

if __name__ == '__main__':
  words = rearrange(sys.argv[1:])
  print(words)