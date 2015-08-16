# -*- coding: utf-8 -*-
__author__ = 'saipc'
l33t_words_to_letters_map = {
    'a' : ['4', '@', '^'],
    'b' : ['8', '13'],
    'c' : ['(', '{' , '<', unicode('€', 'utf-8')],
    'd' : [')', unicode('Ð', 'utf-8')],
    'e' : ['3', unicode('€', 'utf-8')],
    'f' : ['ph'],
    'g' : ['6', '9', '&'],
    'h' : ['#'],
    'i' : ['1', '!', '|'],
    'l' : ['|', '1', unicode('£', 'utf-8')],
    'n' : ['~'],
    'o' : ['0', '*'],
    'q' : ['0', 'o'],
    's' : ['5', '$'],
    't' : ['7', '+'],
    'u' : [unicode('μ', 'utf-8')],
    'w' : ['vv'],
    'x' : ['><'],
    'y' : ['%', unicode('¥', 'utf-8'), 'j'],
    'z' : ['2', 'z', '7']
}
def gen_similar_words(word):
    similar_words = set()
    new_word = word
    for letter in word:
        for leet_letter in l33t_words_to_letters_map[letter.lower()]:
            new_word = new_word.replace(letter, leet_letter)
            similar_words.add(new_word)
    new_word = word
    for letter in reversed(word):
        for leet_letter in l33t_words_to_letters_map[letter.lower()]:
            new_word = new_word.replace(letter, leet_letter)
            similar_words.add(new_word)
    for word in similar_words:
        print(word)



gen_similar_words('suyoce')
