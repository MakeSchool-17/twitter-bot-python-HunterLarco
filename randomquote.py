import random

quotes = ("It's just a flesh wound.", "He's not the Messiah. He's a very naughty boy!", "THIS IS AN EX-PARROT!!")

def random_quote():
  return random.choice(quotes)

if __name__ == '__main__':
  print(random_quote())