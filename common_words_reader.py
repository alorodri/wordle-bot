import fitz
import json
import re

with fitz.open("libros/la_piedra_filosofal.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text().upper()

f = open('word_points.txt', 'r', encoding='utf8')
words: dict = json.load(f)
f.close()

common_words = []
for word in re.findall(r'[A-Z]+', text):
    if word in words.keys() and word not in common_words:
        common_words.append(word)

f = open('common_words.txt', 'w', encoding='utf8')
f.write(json.dumps(common_words, ensure_ascii=False))
f.close()