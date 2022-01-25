# Day 10: 30 Days of python programming
from countries import countries
from countries_data import countries_data

# Loops

# Exercises: Level 1

'''
1. Iterate 0 to 10 using for loop, do the same using while loop.
'''
for num in range(11):
    print('Num: ', num)

counter = 0
while counter <= 10:
    print('Counter: ', counter)
    counter += 1

'''
2. Iterate 10 to 0 using for loop, do the same using while loop.
'''
for num in range(10, -1, -1):
    print('Reverse num: ', num)

while counter >= 0:
    print('Reverse while: ', counter)
    counter -= 1

'''
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
'''
for x in range(7):
    print(x * '#')

'''
4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''
for x in range(8):
    y = ''
    for t in range(8):
        y += '# '
    print(y + '\n')

'''
5. Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
for x in range(11):
    result = x * x
    print(f'{x} x {x} = {result}')

'''
6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
'''
technologies = ['Python', 'Numpy','Pandas','Django', 'Flask']

for tech in technologies:
    print('Tech: ', tech)

'''
7. Use for loop to iterate from 0 to 100 and print only even numbers
'''
for x in range(100):
    if x % 2 == 0:
        print(x)

'''
8. Use for loop to iterate from 0 to 100 and print only odd numbers
'''
for x in range(100):
    if x % 2 != 0:
        print(x)


# Exercises: Level 2

'''
1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
'''
total = 0
for x in range(0, 101):
    total += x

print('Sum of all numbers: ', total)

'''
2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
'''
evens = 0
odds = 0
for x in range(0, 101):
    if (x % 2 == 0):
        evens += x
    else:
        odds += x

print(f'The sum of all evens is {evens}. And the sum of all odds is {odds}.')


# Exercises: Level 3

'''
1. Go to the data folder and use the countries.py file.
Loop through the countries and extract all the countries containing the word land.
'''
land_countries = []
for country in countries:
    if 'land' in country:
        land_countries.append(country)

print('Land countries: ', land_countries)

'''
2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for index in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[index])

print('Reversed fruits: ', reversed_fruits)

'''
3. Go to the data folder and use the countries_data.py file.

    i.   What are the total number of languages in the data
    ii.  Find the ten most spoken languages from the data
    iii. Find the 10 most populated countries in the world
'''
languages = []
spoken_languages = {}
most_spoken_languages = {}
most_populated_countries = {}

for country in countries_data:
    if 'languages' in country and country['languages'] not in languages:
        for language in country['languages']:
            languages.append(language)
            
            if language in spoken_languages:
                spoken_languages[language] += 1
            else:
                spoken_languages[language] = 0

    if 'population' in country:
        if len(most_populated_countries) < 10:
            most_populated_countries[country['name']] = country['population']
        else:
            for (population, x) in most_populated_countries.items():
                if country['population'] > x:
                    del most_populated_countries[population]
                    most_populated_countries[country['name']] = country['population']
                    break

for (language, times) in spoken_languages.items():
    if len(most_spoken_languages) < 10:
        most_spoken_languages[language] = times
    else:
        for (lang, x) in most_spoken_languages.items():
            if times > x:
                del most_spoken_languages[lang]
                most_spoken_languages[language] = times
                break


print('Total number of languages: ', len(set(languages)))
print('Spoken languages: ', spoken_languages)
print('Most spoken languages: ', most_spoken_languages)
print('Most populated countries: ', most_populated_countries)
