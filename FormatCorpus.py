import sys
import random


def stripCorpus(fileurls, outputfile=None):
  totalcorpus = ''
  
  for fileurl in fileurls:
  
    file = open(fileurl, 'r')
    text = file.read()
  
    # remove unnecessary puctuation
    import re
    stripped = re.sub('[^a-zA-Z\s\\.\',]|\n', '', text)
  
    # split into sentences
    sentences = stripped.split('.')
    stripped = ''
  
    # lower first capital
    for sentence in sentences:
      match = re.match('\s*[A-Z]', sentence)
      if not match: continue
      length = len(match.group(0))
      stripped += sentence[:length].lower() + sentence[length:]+'. ' 
  
    # remove multiple spaces, change 'i' to 'I' and 'i'll' to 'I'll'
    stripped = re.sub('\s+', ' ', stripped)
    stripped = re.sub('\si\s', ' I ', stripped)
    stripped = re.sub('\si\'ll\s', ' I ', stripped)

    file.close()
    
    totalcorpus += stripped+' '

  # write it
  if not outputfile:
    outputfile = fileurl
  
  file = open(outputfile, 'w')
  file.write(stripped)
  file.close()



if __name__ == '__main__':
  print(stripCorpus(
    [
      'harrypotter/sorcerers.txt',
      'harrypotter/chamber.txt',
      'harrypotter/azkaban.txt',
      'harrypotter/goblet.txt',
      'harrypotter/phoenix.txt',
      'harrypotter/halfblood.txt',
      'harrypotter/hollows.txt'
    ],
    outputfile='harrypotter/total.txt'
  ))