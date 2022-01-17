# Day 7: 30 Days of python programming

## Sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### Exercises: Level 1
'''
1. Find the length of the set it_companies
'''
print('Length of it_companies: ', len(it_companies))

'''
2. Add 'Twitter' to it_companies
'''
it_companies.add('Twitter')
print('Added Twitter: ', it_companies)

'''
3. Insert multiple IT companies at once to the set it_companies
'''
it_companies.update(['Mirror Studio', 'Hedyla', 'Buildspace'])
print('Added multiple companies: ', it_companies)

'''
4. Remove one of the companies from the set it_companies
'''
it_companies.remove('IBM')
print('Removed IBM: ', it_companies)

'''
5. What is the difference between remove and discard
'''
# Remove throws an error if the item meant to be removed is not in the set.
# Discard doesn't throw any error
it_companies.discard('Hola')

### Exercises: Level 2

'''
1. Join A and B
'''
joint = A.union(B)
print('Joint: ', joint)

'''
2. Find A intersection B
'''
intersection = A.intersection(B)
print('Intersection: ', intersection)

'''
3. Is A subset of B
'''
is_subset = A.issubset(B)
print('Is subset? ', is_subset)

'''
4. Are A and B disjoint sets
'''
are_disjoints = A.isdisjoint(B)
print('Are disjoints? ', are_disjoints)

'''
5. Join A with B and B with A
'''
a_join_b = A.union(B)
print('A joint B: ', a_join_b)

b_join_a = B.union(A)
print('B joint A: ', b_join_a)

'''
6. What is the symmetric difference between A and B
'''
symmetric_difference = A.symmetric_difference(B)
print('Symmetric difference: ', symmetric_difference)

'''
7. Delete the sets completely
'''
del A
del B
print('A and B are deleted now.')

### Exercises: Level 3

'''
1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
'''
ages_set = set(age)
print('Set length: ', len(ages_set))
print('List length: ', len(age))
# List is bigger because it has duplicates

'''
2. Explain the difference between the following data types: string, list, tuple and set
'''
'''
- String: Text. Is mutable.
- List: Collection type. Mutable and can have duplicates. Ordered and indexed.
- Tuple: Collection type. Unmutable and can have duplicates. Ordered and indexed.
- Set: Collection type. Mutable and can't have duplicated. Unordered. 
'''

'''
3. I am a teacher and I love to inspire and teach people.
How many unique words have been used in the sentence?
Use the split methods and set to get the unique words.
'''
sentence = 'I am a teacher and I love to inspire and teach people'
words = len(set(sentence.split(' ')))
print(f'There are {words} unique words.')