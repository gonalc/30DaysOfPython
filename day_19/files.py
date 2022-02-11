# Day 19: 30 Days of python programming

import re
import json
import csv
from stop_words import stop_words

# File Handling

with open('./txt/test.txt') as f:
    print('File: ', f)
    txt = f.read()
    print(txt)

# Exercises: Level 1

'''
1. Write a function which count number of lines and number of words in a text.
All the files are in the data the folder:
    a) Read obama_speech.txt file and count number of lines and words
    b) Read michelle_obama_speech.txt file and count number of lines and words
    c) Read donald_speech.txt file and count number of lines and words
    d) Read melina_trump_speech.txt file and count number of lines and words
'''
def count_words_lines(file_path):
    filename = re.sub('./txt/', '', file_path)
    print('Filename: ', filename)
    with open(file_path) as f:
        lines = f.read().splitlines()
        words = 0
        for line in lines:
            w = re.split(r'\s', line)
            words += len(w)
        print('Lines: ', len(lines))
        print('Words: ', words)


speeches = ['./txt/donald.txt', './txt/melania_trump.txt', './txt/michele_obama.txt', './txt/obama.txt']

for speech in speeches:
    count_words_lines(speech)

'''
2. Read the countries_data.json data file in data directory,
create a function that finds the ten most spoken languages
'''
def most_spoken_languages(filename, amount = 10):
    with open(filename) as f:
        countries = f.read()
        countries = json.loads(countries)

        languages = {}

        for country in countries:
            for language in country['languages']:
                if (language in languages):
                    languages[language] += 1
                else:
                    languages[language] = 1
            
        languages_tuples = [(c[1], c[0]) for c in list(languages.items())]

        most_spoken = sorted(languages_tuples, key = lambda tup: tup[0], reverse = True)
        
        print('Most spoken languages: ', most_spoken[:amount])

most_spoken_languages('../data/countries-data.json')
most_spoken_languages('../data/countries-data.json', 3)

'''
3. Read the countries_data.json data file in data directory,
create a function that creates a list of the ten most populated countries
'''
def most_populated_countries(file_path, amount = 10):
    with open(file_path) as f:
        countries = f.read()
        countries = json.loads(countries)

        population_data = [{ 'country': c['name'], 'population': c['population'] } for c in countries]

        most_populated_sorted = sorted(population_data, key = lambda c: c['population'], reverse = True)

        print('Most populated countries: ', most_populated_sorted[:amount])

most_populated_countries('../data/countries-data.json')
most_populated_countries('../data/countries-data.json', 3)

# Exercises: Level 2

'''
4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
'''
def get_emails():
    with open('../data/email_exchanges_big.txt') as f:
        emails_doc = f.read()
        emails_list = re.findall(r'[\w\d_-]+@\w+\.\w+', emails_doc)

        print('Emails list: ', emails_list)

get_emails()

'''
5. Find the most common words in the English language.
Call the name of your function find_most_common_words,
it will take two parameters - a string or a file and a positive integer,
indicating the number of words. Your function will return an array of
tuples in descending order. Check the output
'''
def find_most_common_words(file_path, amount = 10):
    with open(file_path) as f:
        doc = f.read()
        words = re.split(r'\s', doc)

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

find_most_common_words('../data/sample.txt')
find_most_common_words('../data/sample.txt', 3)

'''
6. Use the function, find_most_frequent_words to find:
    a) The ten most frequent words used in Obama's speech
    b) The ten most frequent words used in Michelle's speech
    c) The ten most frequent words used in Trump's speech
    d) The ten most frequent words used in Melina's speech
'''
find_most_common_words('./txt/donald.txt')
find_most_common_words('./txt/melania_trump.txt')
find_most_common_words('./txt/michele_obama.txt')
find_most_common_words('./txt/obama.txt')

'''
7. Write a python application that checks similarity between two texts.
It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
For instance check the similarity between the transcripts of Michelle's and Melina's speech.
You may need a couple of functions, function to clean the text(clean_text),
function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
List of stop words are in the data directory
'''
def clean_text(filepath):
    with open(filepath) as f:
        doc = f.read()

        words = re.split(r'\s', doc)

        only_words = list(filter(lambda w: re.match(r'^\w+$', w), words))

        return only_words

def remove_support_words(doc):
    filtered = list(filter(lambda w: w not in stop_words, doc))

    return filtered

def check_text_similarity(words1, words2):
    similarities = {}

    for word in words1:
        if word in words2:
            if word in similarities:
                similarities[word] += 1
            else:
                similarities[word] = 1

    tups = [(c[1], c[0]) for c in similarities.items()]

    sorted_words = sorted(tups, key = lambda w: w[0], reverse = True)

    return sorted_words

clean_obama = clean_text('./txt/obama.txt')
removed_support_obama = remove_support_words(clean_obama)

clean_donald = clean_text('./txt/donald.txt')
removed_support_donald = remove_support_words(clean_donald)

print('Similarities: ', check_text_similarity(removed_support_obama, removed_support_donald))

'''
8. Find the 10 most repeated words in the romeo_and_juliet.txt
'''
find_most_common_words('../data/romeo_and_juliet.txt')

'''
9. Read the hacker news csv file and find out:
    a) Count the number of lines containing python or Python
    b) Count the number lines containing JavaScript, javascript or Javascript
    c) Count the number lines containing Java and not JavaScript
'''
def handle_csv(file_path):
    with open(file_path) as f:
        csv_reader = csv.reader(f, delimiter = ',')

        python_lines = 0
        javascript_lines = 0
        java_lines = 0
        for row in csv_reader:
            for word in row:
                has_python = re.search(r'python|Python', word)

                if has_python:
                    python_lines += 1

                has_javascript = re.search(r'Javascript|javascript|JavaScript', word)

                if has_javascript:
                    javascript_lines += 1
                else:
                    has_java = re.search(r'Java$', word)
                    if has_java:
                        java_lines += 1

        
        return {
            'python_lines': python_lines,
            'javascript_lines': javascript_lines,
            'java_lines': java_lines,
        }

print('Hacker result: ', handle_csv('../data/hacker_news.csv'))