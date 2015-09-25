import sys
import random


class MarkovModel:
  
  def __init__(self, text):
    self.text = text
    self.hashmap = {}
    self.words = text.split(' ')
    for i in range(2, len(self.words)):
      self.add(self.words[i-2], self.words[i-1], self.words[i])
  
  def add(self, w1, w2, w3):
    key = hash((w1, w2))
    if not key in self.hashmap:
      self.hashmap[key] = []
    self.hashmap[key].append(w3)
  
  def genWord(self, w1, w2):
    key = hash((w1, w2))
    if not key in self.hashmap:
      return None
    return random.choice(self.hashmap[key])
  
  def random_set(self):
    sentences = self.text.split('. ')
    sentence = []
    while len(sentence) < 2:
      sentence = random.choice(sentences).split(' ')
    return (sentence[0], sentence[1])
  
  def genSentence(self):
    firstset = self.random_set()
    w1 = firstset[0]
    w2 = firstset[1]
    sentence = w1+' '+w2
  
    while w2[-1] != '.':
      new = self.genWord(w1, w2)
      if new == None:
        return self.genSentence()
      w1 = w2
      w2 = new
      sentence += ' '+w2
  
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


if __name__ == '__main__':
  text = open('endersgame.txt', 'r').read()
  model = MarkovModel(text)
  
  for i in range(10):
    print(model.genSentence()+'\n')
