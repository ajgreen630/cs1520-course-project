import logging
import random
from google.cloud import datastore

class WordScrambler():
    def __init__(self):
        """ Initialize word scrambler. """
    
    def get_client(self):
        """ Gets the datastore client. """
        return datastore.Client()

    def get_scrambled_word(self, word):
        """ Returns a scrambled version of a word. """
        scrambled_word = list(word)
        random.shuffle(scrambled_word)
        return ''.join(scrambled_word)

    def word_to_entity(self, word):
        """ Converts a word to an entity. """
        client = self.get_client()

        word_entity = datastore.Entity(client.key('Word'))
        word_entity.update(
            {
                "text":word,
            }
        )
        return word_entity

    def store_words(self, word_list):
        """ Stores a list of words as entities in datastore. """        
        client = self.get_client()

        query = client.query(kind='Word')
        query.add_filter('text', '=', word)
        logging.error('Here are the words in the datastore:')
        datastore_str = '['
        for entity in list(query.fetch()):
            datastore_str += entity['text'] + ','
        datastore_str += ']'
        logging.error(datastore_str)

        for word in word_list:
            query = client.query(kind='Word')
            query.add_filter('text', '=', word)
            if len(list(query.fetch())) == 0:
                client.put(self.word_to_entity(word))
            else:
                logging.error(word + ' is already in the datastore.')

    def get_solution(self, word, guess):
        """ Checks if a users guess to the value of a scrambled word is correct. """
        return word == guess

    def get_random_word(self):
        """ Fetches a random word from the datastore. """
        logging.error('in get random word')
        client = self.get_client()
        query = client.query(kind='Word')
        results = list(query.fetch())
        if len(results) == 0:
            logging.error('results list is empty')
        else:
            logging.error('results list it NOT empty')
        random_word = random.choice(results)

        logging.error(random_word['text'])

        if (isinstance(random_word['text'], bytes)):
            return random_word['text'].decode('UTF-8')
        else:
            return random_word['text']
        #return random_word['text'].decode('UTF-8')