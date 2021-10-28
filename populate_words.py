from word_scrambler import WordScrambler
import logging
import sys

"""
This script stores words in datastore as Word entities.
Usage:
python3 populate_words.py ["WORD1", "WORD2", "WORD3", ...]
"""

def main():
    word_list = ['OAKLAND', 'PITTSBURGH', 'SCHENLEY', 'FRICK', 'MEYRAN', 'FORBES', 'CARNEGIE',
                'PROGRAMMING', 'COMPUTER SCIENCE', 'JAVASCRIPT']
    ws = WordScrambler()
    ws.store_words(word_list)
    logging.error('finished populating database')

if __name__ == "__main__":
    main()

