import sys
import random

quotes = ("It's just a flesh wound.", "He's not the Messiah. He's a very naughty boy!", "THIS IS AN EX-PARROT!!")

def reverse_recurse(word, index):
  if index < 0: return ''
  return word[index] + reverse_recurse(word, index-1)
def reverse(word):
  return reverse_recurse(word, len(word)-1)

if __name__ == '__main__':
  words = reverse(sys.argv[1])
  print(words)