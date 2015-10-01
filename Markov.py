import sys
import random
from HashTable import HashTable


class MarkovModel:
  
  def __init__(self, text, order=1):
    self.text = text
    self.order = order
    self.words = text.split(' ')
    self.hashmap = HashTable(bins=len(self.words))
    
    for i in range(order, len(self.words)):
      self.add(*[self.words[i-j] for j in reversed(range(order+1))])
  
  def add(self, *words):
    prevwords = words[:-1]
    nextword  = words[-1]
    key = hash(prevwords)
    if not self.hashmap.has(key):
      self.hashmap.set(key, [])
    self.hashmap.set(key, self.hashmap.get(key)+[nextword])
  
  def genWord(self, *prevwords):
    key = hash(prevwords)
    if not self.hashmap.has(key):
      return None
    return random.choice(self.hashmap.get(key))
  
  def random_set(self):
    sentences = self.text.split('. ')
    sentence = []
    while len(sentence) < self.order:
      sentence = random.choice(sentences).split(' ')
    return [sentence[i] for i in range(self.order)]
  
  def genSentence(self):
    prevwords = self.random_set()
    sentence = ' '.join(prevwords)
  
    while prevwords[-1][-1] != '.':
      new = self.genWord(*prevwords)
      if new == None:
        return self.genSentence()
      prevwords.pop(0)
      prevwords.append(new)
      sentence += ' '+prevwords[-1]
  
    sentence = sentence[0].upper() + sentence[1:]
    return sentence


# Naw, you don't care, so you sring out your body or no one has ever tried because they're having a Third, turd.
# Looks like you're big time now, can't play with you all in every battle, and today you finally fought them under him.
# Nonsense, Ender, Anderson said softly.
# Then he made himself dictator, and died in Battle School.
# Valentine kissed him and me.
# His answer would be no part of the door, still wet from his dreams, but they aren't commanders, they don't want you screwing around with Ender's fluid, unpatterned attack.
# Then I turned around again and again a blow to the forcefield of the human race.
# There was something else he needed, assign them to withdraw, they withdrew, knowing that she didn't answer.
# Mazer, I don't think you're taking this all too seriously, said Mother.
# Only the enemy knows exactly where you are unpleasantly fat.
# Americans are quite apt at playing stupid when they made fun of me that somebody's willing to kill, but it helps narrow the number of people really angry.
# You aren't worth the price you pay.
# No radioactivity, no mess.
# He feels your neglect of strategy.


if __name__ == '__main__':
  # text = open('harrypotter/total.txt', 'r').read()
  text = open('harrypotter/total.txt', 'r').read()
  model = MarkovModel(text, order=2)
  
  for i in range(10):
    print(model.genSentence()+'\n')
