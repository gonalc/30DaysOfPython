# Day 20: 30 Days of python programming

# Packages

import re
import requests

def find_most_common_words(text, amount = 10):
    words = re.split(r'\s', text)

    words_dict = {}

    for word in words:
        if len(word) > 0:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    word_tups = [(c[1], c[0]) for c in words_dict.items()]

    sorted_words = sorted(word_tups, key = lambda c: c[0], reverse = True)
    print('Most common words: ', sorted_words[:amount])

# Exercises: Level 1

'''
1. Read this url and find the 10 most frequent words. 
'''
romeo_juliet_url = 'http://www.gutenberg.org/files/1112/1112.txt'

romeo_juliet = requests.get(romeo_juliet_url)

romeo_juliet = romeo_juliet.text

find_most_common_words(romeo_juliet)

'''
2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :

    the min, max, mean, median, standard deviation of cats' weight in metric units.
    the min, max, mean, median, standard deviation of cats' lifespan in years.
    Create a frequency table of country and breed of cats
'''
cats = requests.get('https://api.thecatapi.com/v1/breeds').json()

def get_cat_weight(cat):
    if 'weight' in cat and 'metric' in cat['weight']:
        min_weight, max_weight = re.split(r'\s-\s', cat['weight']['metric'])
        
        return (int(min_weight), int(max_weight))


def get_cat_data():
    weights = [get_cat_weight(c) for c in cats]
    mins = [w[0] for w in weights]
    maxs = [w[1] for w in weights]
    min_weight = min(mins)
    max_weight = max(maxs)
    print('Min weight: ', min_weight)
    print('Max weight: ', max_weight)

get_cat_data()
