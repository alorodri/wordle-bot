import json

from utils import MapUtils

f = open('words.txt', 'r', encoding='utf8')
all_words: dict = json.load(f)
f.close()

letters_percents = {}

total_letters = {}
quantity_letters_in_pos = [
    {}, {}, {}, {}, {}
]
letters_quantity = 0
for word_list in all_words.values():
    for word in word_list:
        for idx, letter in enumerate(word):
            MapUtils.increment_map_value(total_letters, letter)
            MapUtils.increment_map_value(quantity_letters_in_pos[idx], letter)
            letters_quantity += 1

for letter, quantity in total_letters.items():
    letters_percents[letter + '_all'] = quantity * 100 / letters_quantity

for idx, position in enumerate(quantity_letters_in_pos):
    for letter, quantity in position.items():
        letters_percents[letter + '_' + str(idx+1)] = quantity * 100 / letters_quantity

f = open('words_stats.txt', 'w', encoding='utf8')
f.write(json.dumps(letters_percents, ensure_ascii=False))
f.close()

word_points = {}
for word_list in all_words.values():
    for word in word_list:
        points = 0
        existing_letters = []
        for idx, letter in enumerate(word):
            points += letters_percents[letter + '_all']
            points += letters_percents[letter + '_' + str(idx+1)]
            if letter not in existing_letters:
                points += 10
            existing_letters.append(letter)

        word_points[word] = points

f = open('word_points.txt', 'w', encoding='utf8')
f.write(json.dumps(word_points, ensure_ascii=False))
f.close()