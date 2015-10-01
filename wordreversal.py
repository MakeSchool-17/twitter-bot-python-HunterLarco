import sys
import random

def reverse_recurse(word, index):
  if index < 0: return ''
  return word[index] + reverse_recurse(word, index-1)
def reverse(word):
  return reverse_recurse(word, len(word)-1)

if __name__ == '__main__':
  text = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'This is a test.'
  words = reverse(text)
  print(words)