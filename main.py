import flask
from word_scrambler import WordScrambler

# Execution:
# 1. gcloud config set project [PROJECT_ID] (for each terminal)
# 2. gcloud app deploy [us-east1]
# 3. dev_appserver.py app.yaml

ws = WordScrambler()
word = ''
scrambled_word = ''

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index.html')
@app.route('/index')
def root():
    return flask.render_template('index.html', page_title='Room of Doubt')

@app.route('/panther-central.html')
def get_word_scramble():
    word = ws.get_random_word()
    scrambled_word = ws.get_scrambled_word(word)
    return flask.render_template('panther-central.html', page_title='Panther Central', scramble_val=scrambled_word)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)




