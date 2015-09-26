#!flask/bin/python
from flask import Flask
app = Flask(__name__, static_folder='resources')

from flask import request
from flask import render_template
from Markov import MarkovModel





print('Loading Corpus')
text = open('harrypotter/total.txt', 'r').read()
model = MarkovModel(text, order=2)
print('Model Ready')






@app.route('/sentences/')
def server_sentences():
  count = int(request.args.get('count') or 1)
  try:    minwords = int(request.args.get('minwords'))
  except: minwords = None
  try:    maxwords = int(request.args.get('maxwords'))
  except: maxwords = None
  return prettify(query_sentences(count, minwords, maxwords))

@app.route('/')
def server_static():
  return render_template('main.html', sentences=query_sentences(2))





def prettify(obj):
  from json import dumps
  return dumps(obj, indent=2, sort_keys=True)

def query_sentences(count, minwords=None, maxwords=None):
  minwords = minwords or 5
  maxwords = maxwords or 25
  return [model.genSentence(minwords=minwords, maxwords=maxwords) for _ in range(count)]
  




if __name__ == '__main__':
  app.run(debug=True)