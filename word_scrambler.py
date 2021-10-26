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
            "text" : word
        )
        return word_entity

    def store_words(self, word_list):
        """ Stores a list of words as entities in datastore. """
        client = self.get_client()
        for word in word_list:
            query = client.query(kind='Word')
            query.add_filter('text', '=', word)
            if len(list(query.fetch())) == 0:
                client.put(self.word_to_entity(word))

    def get_solution(self, word, guess):
        """ Checks if a users guess to the value of a scrambled word is correct. """
        return word == guess

    def get_random_word(self):
        """ Fetches a random word from the datastore. """
        client = self.get_client()

        query = client.query(kind='Word')
        random_word = random.choice(list(query.fetch()))

        return random_word['text'].decode('UTF-8')