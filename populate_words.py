from word_scrambler import WordScrambler
import sys

"""
This script stores words in datastore as Word entities.
Usage:
python3 populate_words.py ["WORD1", "WORD2", "WORD3", ...]
"""

def main():
    word_list = sys.argv[1]

    ws = WordScrambler()
    ws.store_words()

if __name__ == "__main__":
    main()

