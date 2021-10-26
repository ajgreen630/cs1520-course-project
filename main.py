import flask
import word_scrambler

# Execution:
# 1. gcloud config set project [PROJECT_ID] (for each terminal)
# 2. gcloud app deploy [us-east1]
# 3. dev_appserver.py app.yaml

ws = word_scrambler.WordScrambler()
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

@app.route('/hillman-library.html')
def hillman_library():
    return flask.render_template('hillman-library.html', page_title='Hillman Library')

@app.route('/hillman2.html')
def hillman2():
    return flask.render_template('hillman2.html', page_title='Hillman Library')

@app.route('/hillman3.html')
def hillman3():
    return flask.render_template('hillman3.html', page_title='Hillman Library')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)




