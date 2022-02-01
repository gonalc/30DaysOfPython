# Day 10: 30 Days of python programming

# List Comprehension

# Exercises: Level 1

'''
1. Filter only negative and zero in the list using list comprehension
'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print('Negative and zero: ', negative_and_zero)

'''
2. Flatten the following list of lists of lists to a one dimensional list :

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [num for outter in list_of_lists for row in outter for num in row]
print('Flatten list: ', flatten_list)

'''
3. Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''
def tuple_generator(num, amount = 6):
    nums = [num]
    for x in range(amount):
        res = num ** x
        nums.append(res)

    return tuple(nums)

list_of_tuples = [tuple_generator(i) for i in range(11)]
print('List of Tuples: ', list_of_tuples)

'''
4. Flatten the following list to a new list:
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def country_parser(country_tuple):
    country, city = country_tuple

    return [country.upper(), country[:3].upper(), city.upper()]

parsed_countries = [country_parser(i) for row in countries for i in row]
print('Parsed countries: ', parsed_countries)

'''
5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
'''
def dictionarize_countries(c):
    country, city = c
    return {
        'country': country,
        'city': city
    }

countries_dict = [dictionarize_countries(i) for row in countries for i in row]
print('Dictionary of countries: ', countries_dict)

'''
6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
'''
def concat_name(n):
    name, last_name = n
    return lambda: f'{name} {last_name}'
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

concatenated_names = [concat_name(n)() for row in names for n in row]
print('Concatenated names: ', concatenated_names)