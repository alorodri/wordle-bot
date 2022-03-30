from constants import Constants
import json
from random import randrange
import re
from words import PERCENTS

from test import Test

f = open('words.txt', 'r', encoding='utf8')
words: dict = json.load(f)

class Solver():

    __letters_not_in_word = []
    __letters_in_other_pos = {}
    __letters_correct_pos = [None] * 5
    __test = Test()
    __tried_letters = {}

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

    @staticmethod
    def check_is_in_map_list(m, k, v):
        if k not in m.keys():
            return False
        elif v not in m[k]:
            return False
        return True

    @staticmethod
    def add_to_list(m, k, v):
        if k in m.keys():
            m[k].append(v)
        else:
            m[k] = [v]                

    def solve(self, regex):
        print(f'Starting with pattern {regex}')
        regex_words = self.return_words_regex(regex)
        if len(regex_words):
            rand = randrange(len(regex_words))
            word_attempt = regex_words[rand]
            if word_attempt:
                print(f'Trying {word_attempt} (pattern was {regex})')
                self.__colors = self.__test.try_attempt(word_attempt)

                for idx, color in enumerate(self.__colors):
                    if color == Constants.YELLOW:
                        self.add_to_list(self.__letters_in_other_pos, word_attempt[idx], idx)
                    elif color == Constants.GREEN:
                        self.__letters_correct_pos[idx] = word_attempt[idx]
                    elif color == Constants.GRAY:
                        self.__letters_not_in_word.append(word_attempt[idx])

        if not self.__colors:
            return
        if Constants.GRAY not in self.__colors and Constants.YELLOW not in self.__colors:
            print('SOLVED')
            return

        word = ''
        for idx in range(0, 5):

            next_loop = False

            if self.__letters_correct_pos[idx]:
                word += self.__letters_correct_pos[idx]
                continue

            for letter, pos in self.__letters_in_other_pos.items():
                if idx != pos and letter not in word:
                    word += letter
                    next_loop = True
                    break

            if next_loop:
                continue

            if idx > 0:
                word += '.'
                continue

            for letter in PERCENTS.keys():
                if (letter not in self.__letters_not_in_word
                    and not self.check_is_in_map_list(self.__letters_in_other_pos, letter, idx)
                    and not self.check_is_in_map_list(self.__tried_letters, letter, idx)):
                    word += letter
                    self.add_to_list(self.__tried_letters, letter, idx)
                    break
        
        self.solve(word)
        

solver = Solver()
solver.solve('OREAS')