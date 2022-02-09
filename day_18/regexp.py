# Day 18: 30 Days of python programming

# Regular Expressions

# Exercises: Level 1

import re

'''
1. What is the most frequent word in the following paragraph?
'''
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
splitted = re.findall(r'\w+', paragraph)
dictionary = {}
for word in splitted:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

tups = []
for k, v in dictionary.items():
    tups.append((v, k))

sorted_tups = sorted(tups, key = lambda t: t[0], reverse = True)

print('Tups: ', sorted_tups)

'''
2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1
in the negative direction, 0 at origin, 4 and 8 in the positive direction.
Extract these numbers from this whole text and find the distance between the two furthest particles.
'''
txt = '''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1
in the negative direction, 0 at origin, 4 and 8 in the positive direction.
Extract these numbers from this whole text and find the distance between the two furthest particles.'''

nums = list(map(lambda x: int(x), re.findall(r'\d|-\d', txt)))
leftiest = min(nums)
rightest = max(nums)
distance = rightest - leftiest
print('Min: ', leftiest)
print('Max: ', rightest)
print('nums: ', nums)
print('Distance: ', distance)

# Exercises: Level 2

'''
1. Write a pattern which identifies if a string is a valid python variable
'''
def is_valid_variable(text):
    try:
        starts_with_letter = bool(re.match(r'^[a-z]', text))
        no_specials = not bool(re.search(r'[^\w|_]', text))
        no_caps = not bool(re.search(r'[A-Z]+', text))
        
        return starts_with_letter and no_specials and no_caps
    except Exception as e:
        print('Please, enter a valid text: ', e)
    
print('Valid? ', is_valid_variable('first_name')) # True
print('Valid?', is_valid_variable('first-name')) # False
print('Valid?', is_valid_variable('1first_name')) # False
print('Valid?', is_valid_variable('firstname')) # True

# Exercises: Level 3

'''
1. Clean the following text. After cleaning, count three most frequent words in the string.
'''
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple.
;I found tea@ching m%o@re interesting tha@n any other %jo@bs.
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean = re.sub(r'[^\w\s]', '', sentence)

def count_words(text):
    splitted = re.findall(r'\w+', text)
    dictionary = {}
    for word in splitted:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    tups = []
    for k, v in dictionary.items():
        tups.append((v, k))

    sorted_tups = sorted(tups, key = lambda t: t[0], reverse = True)

    return sorted_tups

print('Clean: ', clean)
print('Counted words: ', count_words(clean))