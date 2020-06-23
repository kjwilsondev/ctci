import os
import sys
import itertools

class Text:
    def __init__(self, text):
        """
        Loads words from dictionary
        """
        # Dictionary shortcut
        # wordList = [line.strip() for line in open('/usr/share/dict/words')]

        file  = open(text, 'r')
        loads = file.readlines()
        self.words = [word.strip() for word in loads]
        file.close()
        self.unique_words, self.unique_word_count = self.update_unique_words()

        print("successfully loaded text")
        
    def update_unique_words(self):
        """
        Creates set of unique words with
        non-repeating letters
        """
        unique_words = set()
        unique_word_count = 0
        for word in self.words:
            if is_unique(word):
                unique_word_count += 1
                unique_words.add(word)
        return unique_words, unique_word_count
    
def is_unique(word):
    for letter in range(0,len(word)-2):
       for compare in range(letter + 1,len(word)-1):
            if word[letter] == word[compare]:
                return False
            if compare < len(word):
                compare += 1
    return True

if __name__ == "__main__":
    dictionary = Text("/usr/share/dict/words")
    print(dictionary.unique_word_count)
    # print(is_unique("calyculated"))