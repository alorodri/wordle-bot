import json
import lxml.html
import requests

words = {}
for pagina_number in range(1, 14):
    if pagina_number == 1:
        nombre_pagina = ''
    else:
        nombre_pagina = 'pagina' + str(pagina_number)
    html = requests.get(f'https://www.listasdepalabras.es/palabras5letras{nombre_pagina}.htm')
    doc = lxml.html.fromstring(html.content)

    new_releases = doc.xpath('//table//span[@class="mot"]')[0]
    words_arr = new_releases.text.split(' ')
    for word in words_arr:
        first_letter = word[0]
        if first_letter in words.keys():
            words[first_letter].append(word)
        else:
            words[first_letter] = []
            words[first_letter].append(word)

f = open('words.txt', 'w', encoding='utf8')
f.write(json.dumps(words, ensure_ascii=False))
f.close()