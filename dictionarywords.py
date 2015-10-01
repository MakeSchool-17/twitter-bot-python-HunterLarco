import sys
import random

dictionary = open('/usr/share/dict/words').read().split('\n')

def randomword():
  return random.choice(dictionary)

def random_words(numwords=1):
  return [randomword() for _ in range(numwords)]

if __name__ == '__main__':
  numwords = int(sys.argv[1] if len(sys.argv) > 1 else 10)
  words = random_words(numwords)
  print(words)