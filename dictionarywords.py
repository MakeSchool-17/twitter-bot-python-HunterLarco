import sys
import random

dictionary = open('/usr/share/dict/words').read().split('\n')

def randomword():
  return random.choice(dictionary)

if __name__ == '__main__':
  numwords = int(sys.argv[1])
  words = [randomword() for i in range(numwords)]
  print(words)