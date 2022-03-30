from constants import Constants
import json
from random import randrange
import re

from test import Test

f = open('words.txt', 'r', encoding='utf8')
words: dict = json.load(f)

class Solver():

    __letters_not_in_word = []
    __letters_in_word = []
    __word = ''
    __test = Test()

    def __init__(self) -> None:
        pass

    def return_words_containing(self, letters):
        result = []
        for key in words:
            for word in words[key]:
                matches = 0
                for letter in letters:
                    if letter in word:
                        matches += 1
                if matches == len(letters):
                        result.append(word)

        return result

    def return_words_regex(self, regex):
        result = []
        for key in words:
            for word in words[key]:
                match = re.findall(regex, word)
                if match:
                    result += match

        return result
                

    def solve(self, regex):
        regex_words = self.return_words_regex(regex)
        rand = randrange(len(regex_words))
        colors = self.__test.try_attempt(regex_words[rand])

        # Return an object with word like now, and with letters that are in the word but in other position
        # Save all the letters that aren't in the word, so we don't use them again

        if not colors:
            return
        if Constants.GRAY not in colors and Constants.YELLOW not in colors:
            print('SOLVED')
            return
        
        self.solve('')
        

solver = Solver()
solver.solve('OREAS')