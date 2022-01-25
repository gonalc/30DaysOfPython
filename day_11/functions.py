# Day 10: 30 Days of python programming
from countries_data import countries_data

# Functions

# Exercises: Level 1

'''
1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
'''
def add_two_numbers(num1, num2):
    return num1 + num2

print('Sum: ', add_two_numbers(14, 27))

'''
2. Area of a circle is calculated as follows: area = π x r x r.
Write a function that calculates area_of_circle.
'''
def circle_area(r):
    return 3.14 * r * r

print('Circle area: ', circle_area(3))

'''
3. Write a function called add_all_nums which takes arbitrary number of
arguments and sums all the arguments. Check if all the list items are number types.
If not do give a reasonable feedback.
'''
def add_all_nums(*nums):
    sum = 0
    for n in nums:
        if type(n) == int or type(n) == float:
            sum += float(n)
        else:
            print(f'{n} is not a number.')
    return sum

print('Sum numbers: ', add_all_nums(1, 4.5, 17))
print('Sum with intrusos: ', add_all_nums(10, 14, 'hola', 90))

'''
4. Temperature in °C can be converted to °F using this formula:
°F = (°C x 9/5) + 32. Write a function which converts °C to °F,
convert_celsius_to-fahrenheit.
'''
def convert_celsius_to_fahrenheit(celsius):
    return celsius * (9 / 5)

print('Celsius to Fahrenheit: ', convert_celsius_to_fahrenheit(35))

'''
5. Write a function called check-season,
it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
'''
def check_season(month):
    if month == 'december' or month == 'january' or month == 'february':
        return 'Winter'
    elif month == 'march' or month == 'april' or month == 'may':
        return 'Spring'
    elif month == 'june' or month == 'july' or month == 'august':
        return 'Summer'
    else:
        return 'Autumn'

print('Season: ', check_season('march'))

'''
6. Write a function called calculate_slope which return the slope of a linear equation
'''
# no idea what the slop is

'''
7. Quadratic equation is calculated as follows: ax² + bx + c = 0.
Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
'''
def solve_quadratic_eqn(a, b, c):
    # ax² + bx + c = 0
    print('No idea')

'''
8. Declare a function named print_list.
It takes a list as a parameter and it prints out each element of the list.
'''
def print_list(list):
    for item in list:
        print('ITEM: ', item)

print_list(['hola', 'adios'])

'''
9. Declare a function named reverse_list.
It takes an array as a parameter and it returns the reverse of the array (use loops).
'''
def reverse_list(list):
    for index in range(len(list) - 1, -1, -1):
        print('Reversed: ', list[index])

reverse_list(['hola', 'adios'])

'''
10. Declare a function named capitalize_list_items.
It takes a list as a parameter and it returns a capitalized list of items
'''
def capitalize_list_items(list):
    capitalized = []
    for item in list:
        capitalized.append(item.capitalize())
    return capitalized

print('Capitalized: ', capitalize_list_items(['gonzalo', 'alcaide', 'gimenez']))

'''
11. Declare a function named add_item. It takes a list and an item parameters.
It returns a list with the item added at the end.
'''
def add_item(list, item):
    copy_list = list.copy()
    copy_list.append(item)

    return copy_list

print('Added item: ', add_item([1, 2, 3], 4))

'''
12. Declare a function named remove_item. It takes a list and an item parameters.
It returns a list with the item removed from it.
'''
def remove_item(list, item):
    copied = list.copy()
    copied.remove(item)

    return copied

print('Removed item: ', remove_item(['hola', 'adios', 'quetal'], 'adios'))

'''
13. Declare a function named sum_of_numbers.
It takes a number parameter and it adds all the numbers in that range.
'''
def sum_of_numbers(num):
    sum = 0
    for n in range(num + 1):
        sum += n
    return sum

print('Sum all numbers [5]: ', sum_of_numbers(5))
print('Sum all numbers [10]: ', sum_of_numbers(10))
print('Sum all numbers [100]: ', sum_of_numbers(100))

'''
14. Declare a function named sum_of_odds.
It takes a number parameter and it adds all the odd numbers in that range.
'''
def sum_of_odds(num):
    sum = 0
    for n in range(num + 1):
        if n % 2 != 0:
            sum += n
    return sum

print('Sum all odds: ', sum_of_odds(100))

'''
15. Declare a function named sum_of_even.
It takes a number parameter and it adds all the even numbers in that - range.
'''
def sum_of_even(num):
    sum = 0
    for n in range(num + 1):
        if n % 2 == 0:
            sum += n
    return sum

print('Sum all even: ', sum_of_even(100))

# Exercises: Level 2

'''
1. Declare a function named evens_and_odds.
It takes a positive integer as parameter and it counts number of evens and odds in the number.
'''
def evens_and_odds(num):
    odds = 0
    evens = 0

    for n in range(num + 1):
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
        
    print(f'The number of odds is: {odds}')
    print(f'The number of evens is: {evens}')

evens_and_odds(100)

'''
2. Call your function is_empty, it takes a parameter and it checks if it is empty or not
'''
def is_empty(element):
    return len(element) == 0

print('Is empty? ', is_empty([]))
print('Is empty? ', is_empty(''))
print('Is empty? ', is_empty({}))

# Exercises: Level 3

'''
1. Write a function called is_prime, which checks if a number is prime.
'''
def is_prime(num):
    prime = num

    for n in range(num - 1, 1, -1):
        rest = num % n
        if rest < prime:
            prime = rest
    
    return prime != 0
print('Is prime? ', is_prime(37))

'''
2. Write a functions which checks if all items are unique in the list.
'''
def all_unique(list):
    check = []
    for item in list:
        if item in check:
            return False
        else:
            check.append(item)
    
    return True

print('Are items unique? ', all_unique([1, 2, 3]))
print('Are items unique? ', all_unique([1, 2, 3, 3]))

'''
3. Write a function which checks if all the items of the list are of the same data type.
'''
def same_type(list):
    check = type(list[0])
    for item in list:
        if type(item) != check:
            return False
    
    return True

print('Same type? ', same_type([1, 2, 3, 4]))
print('Same type? ', same_type([1, 2, 3, '4']))

'''
4. Write a function which check if provided variable is a valid python variable
'''
def is_valid_variable(item):
    return item.isidentifier()
print('Is valid as variable name? ', is_valid_variable('hola'))
print('Is valid as variable name? ', is_valid_variable('34'))

'''
5. Go to the data folder and access the countries-data.py file.

    * Create a function called the most_spoken_languages in the world.
    It should return 10 or 20 most spoken languages in the world in descending order
    
    * Create a function called the most_populated_countries.
    It should return 10 or 20 most populated countries in descending order.
'''
def most_spoken_languages(max_length = 10):
    languages = {}
    for country in countries_data:
        if 'languages' in country:
            for language in country['languages']:
                if language in languages:
                    languages[language] += 1
                else:
                    languages[language] = 0
        
    most_spoken_list = {}
    for (lang, countries) in languages.items():
        if len(most_spoken_list) < max_length:
            most_spoken_list[lang] = countries
        else:
            for (l, k) in most_spoken_list.items():
                if k < countries:
                    del most_spoken_list[l]
                    most_spoken_list[lang] = countries
                    break

    sorted_list_tuples = sorted(list(most_spoken_list.items()), key=lambda tup: tup[1], reverse=True)
    final_list = []
    for item in sorted_list_tuples:
        final_list.append(item[0])

    return final_list

print('Most spoken languages: ', most_spoken_languages(10))

def most_populated_countries(max_length = 10):
    population_list = []
    for country in countries_data:
        if len(population_list) < max_length:
            population_list.append((country['name'], country['population']))
        else:
            for c in population_list:
                if c[1] < country['population']:
                    index = [y[0] for y in population_list].index(c[0])
                    del population_list[index]
                    population_list.append((country['name'], country['population']))
                    break

    sorted_list_tuples = sorted(population_list, key=lambda tup: tup[1], reverse=True)

    final_list = []
    for item in sorted_list_tuples:
        final_list.append(item[0])

    return final_list

print('Population list: ', most_populated_countries())