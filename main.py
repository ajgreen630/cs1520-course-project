import flask
import word_scrambler
import populate_words
import logging
from google.cloud import datastore
import os
import json

# Execution:
# 1. gcloud config set project [PROJECT_ID] (for each terminal)
# 2. gcloud app deploy [us-east1]
# 3. dev_appserverpy app.yaml

# TODO: Add code for populating datastore if running on local (dev_appserver).
ws = word_scrambler.WordScrambler()
username = ""
email = ""
password = ""

app = flask.Flask(__name__)

# Redirect to title page upon first entry:
@app.route('/')
@app.route('/title')
@app.route('/title.html')
def root():
    return flask.render_template('title.html')

@app.route('/introduction')
@app.route('/introduction.html')
def intro():
    return flask.render_template('introduction.html')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/loginPage.html', methods=['GET', 'POST'])
def login():
    return flask.render_template('loginPage.html')

@app.route('/register', methods=['POST']) 
def register():
    logging.error("In register!")
    data = flask.request.get_json()
    logging.error(type(data))
    logging.error(data)
    logging.error(data["username"])
    logging.error(data["email"])
    logging.error(data["password"])

    # After inserting into DB, redirect to /login:
    return flask.render_template('loginPage.html')

# Redirect to panther-central.html:
@app.route('/panther-central')
@app.route('/panther-central.html')
def get_word_scramble():
    word = ws.get_random_word() # Get random word from datastore.
    scrambled_word = ws.get_scrambled_word(word)    # Scramble the word.

    return flask.render_template('panther-central.html', 
                                  page_title = 'Panther Central', 
                                  scrambled_word = scrambled_word,
                                  unscrambled_word = word)

@app.route('/hillman-library')
@app.route('/hillman-library.html')
def hillman_library():
    return flask.render_template('hillman-library.html', page_title='Hillman Library')

@app.route('/hillman1')
@app.route('/hillman1.html')
def hillman1():
    return flask.render_template('hillman1.html', page_title='Hillman Library')

@app.route('/hillman2')
@app.route('/hillman2.html')
def hillman2():
    return flask.render_template('hillman2.html', page_title='Hillman Library')

@app.route('/hillman3')
@app.route('/hillman3.html')
def hillman3():
    return flask.render_template('hillman3.html', page_title='Hillman Library')

@app.route('/map1')
@app.route('/map1.html')
def map1():
    return flask.render_template('map1.html', page_title='Hillman Library')

@app.route('/map2')
@app.route('/map2.html')
def map2():
    return flask.render_template('map2.html', page_title='Hillman Library')

@app.route('/map3')
@app.route('/map3.html')
def map3():
    return flask.render_template('map3.html', page_title='Hillman Library')

@app.route('/sennott-square')
@app.route('/sennott-square.html')
def sennott_square():
    return flask.render_template('sennott-square.html', page_title='Sennott Square')

#TODO: Add Hall of Fame page (leaderboard)
@app.route('/hof')
@app.route('/halloffame')
@app.route('/halloffame.html')
def hall_of_fame():
    return flask.render_template('halloffame.html')

@app.route('/congratulations.html')
def congratulations():
    return flask.render_template('congratulations.html', page_title='Congratulations!')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)




