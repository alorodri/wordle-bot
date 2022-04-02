from constants import Constants
import json
import re
from utils import MapUtils
from words import PERCENTS

from test import Test

f = open('words.txt', 'r', encoding='utf8')
words: dict = json.load(f)
f.close()

f = open('words_stats.txt', 'r', encoding='utf8')
stats: dict = json.load(f)
f.close()

class Solver():

    __letters_not_in_word = []
    __letters_in_other_pos = {}
    __test = Test()
    __word_scores = {}

    def __init__(self) -> None:      
        f = open('word_points.txt', 'r', encoding='utf8')
        self.__word_scores = json.load(f)
        f.close()

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

    def not_in_word_filter(self, word):
        for letter in word:
            if letter in self.__letters_not_in_word:
                return False

        return True

    def in_other_pos_filter(self, word):
        for idx, letter in enumerate(word):
            filter = MapUtils.check_is_in_map_list(self.__letters_in_other_pos, letter, idx)
            if filter:
                return False
        
        return True

    def solve(self, regex):
        regex_words = self.return_words_regex(regex)
        regex_words = list(filter(self.not_in_word_filter, regex_words))
        regex_words = list(filter(self.in_other_pos_filter, regex_words))
        if len(regex_words):
            regex_words.sort(reverse=True, key=lambda w: self.__word_scores[w])
            word_attempt = regex_words[0]
            colors = self.__test.try_attempt(word_attempt)
            print(f'Trying with word {word_attempt}')

            if colors.count(Constants.GREEN) == 5:
                print('GAME WON')
                return

            for idx, color in enumerate(colors):
                if color == Constants.GREEN:
                    regex = regex[:idx] + word_attempt[idx] + regex[idx+1:]
                elif color == Constants.YELLOW:
                    MapUtils.add_to_mapvalue_list(self.__letters_in_other_pos, word_attempt[idx], idx)
                else:
                    self.__letters_not_in_word.append(word_attempt[idx])

        self.solve(regex)
                
        
solver = Solver()
solver.solve('.....')