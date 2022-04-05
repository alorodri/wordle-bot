from constants import Constants
import json
import re
from explorer import Explorer
from utils import MapUtils

from test import Test

USE_COMMONS = True

f = open('words.txt', 'r', encoding='utf8')
words: dict = json.load(f)
f.close()

f = open('words_stats.txt', 'r', encoding='utf8')
stats: dict = json.load(f)
f.close()

f = open('common_words.txt', 'r', encoding='utf8')
common: list = json.load(f)
f.close()

class Solver():

    __letters_not_in_word = []
    __letters_in_other_pos = {}
    __word_scores = {}
    __attempt = 1
    __explorer = None

    def __init__(self) -> None:      
        f = open('word_points.txt', 'r', encoding='utf8')
        self.__word_scores = json.load(f)
        f.close()
                
        self.__explorer = Explorer()
        self.__explorer.navigate()

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
            if USE_COMMONS:
                for word in regex_words:
                    if word in common:
                        word_attempt = word
                        break

            colors = self.__explorer.attempt(word_attempt, self.__attempt)

            if colors.count(Constants.GREEN) == 5:
                print(f'Game ended, word was "{word_attempt}"')
                return

            for idx, color in enumerate(colors):
                if color == Constants.GREEN:
                    regex = regex[:idx] + word_attempt[idx] + regex[idx+1:]
                elif color == Constants.YELLOW:
                    MapUtils.add_to_mapvalue_list(self.__letters_in_other_pos, word_attempt[idx], idx)
                else:
                    if word_attempt[idx] not in self.__letters_in_other_pos:
                        # bug del wordle, en el que si intentas la letra varias veces y no aciertas la posición
                        # exacta en ninguna, te sale la primera como amarilla y las siguientes como ausente
                        self.__letters_not_in_word.append(word_attempt[idx])
                    else:
                        MapUtils.add_to_mapvalue_list(self.__letters_in_other_pos, word_attempt[idx], idx)

        self.__attempt += 1
        self.solve(regex)

solver = Solver()
solver.solve('.....')