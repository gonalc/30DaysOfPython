# Day 10: 30 Days of python programming

# High order functions


from functools import reduce
from countries import countries as all_countries

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

'''
1. Explain the difference between map, filter, and reduce.
'''
'''
* map: receives a function and an iterable. Returns a list with the result of the function for each item.
* filter: same as map but the passed function returns a boolean and the returned list only has the items whose 
function result has been True.
* reduce: returns a single value.
'''

'''
2. Explain the difference between higher order function, closure and decorator
'''
'''
* higher order function: a function that receives a function as a param.
* closure: inner function in a function. Can access the variables in the outer scope.
* decorator: Design pattern to add new functionality to functions without modifying its structure.
'''

'''
3. Define a call function before map, filter or reduce, see examples.
'''
'''
def uppercase(item):
    return item.upper()
result = map(uppercase, countries)
'''

'''
4. Use for loop to print each country in the countries list.
'''
for country in countries:
    print('Country: ', country)

'''
5. Use for to print each name in the names list.
'''
for name in names:
    print('Name: ', name)

'''
6. Use for to print each number in the numbers list.
'''
for num in numbers:
    print('Number: ', num)


# Exercises: Level 2

'''
1. Use map to create a new list by changing each country to uppercase in the countries list
'''
uppercase_countries = map(lambda country: country.upper(), countries)
print('Uppercase countries: ', uppercase_countries)

'''
2. Use map to create a new list by changing each number to its square in the numbers list
'''
squared = map(lambda n: n ** 2, numbers)
print('Squared: ', squared)

'''
3. Use map to change each name to uppercase in the names list
'''
uppercase_names = map(lambda name: name.upper(), names)
print('Uppercased names: ', uppercase_names)

'''
4. Use filter to filter out countries containing 'land'.
'''
no_land_countries = filter(lambda c: 'land' not in c, countries)
print('No land countries: ', no_land_countries)

'''
5. Use filter to filter out countries having exactly six characters.
'''
no_six_char_countries = filter(lambda c: len(c) != 6, countries)
print('No six characters countries: ', no_six_char_countries)

'''
6. Use filter to filter out countries containing six letters and more in the country list.
'''
small_names_countries = filter(lambda c: len(c) < 6, countries)
print('Small names countries: ', small_names_countries)

'''
7. Use filter to filter out countries starting with an 'E'
'''
no_e_countries = filter(lambda c: c[0] != 'E', countries)
print('No starting with E countries: ', no_e_countries)

'''
8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
'''
chained = reduce(lambda x, y: x + ' _ ' + y, filter(lambda c: c[0] != 'E', map(lambda c: c.upper(), countries)))
print('Chained: ', chained)

'''
9. Declare a function called get_string_lists which takes a list as a parameter
and then returns a list containing only string items.
'''
mixed_list = [1, 'hola', { 'id': 3 }, ('key', 'value'), 'adios']

def get_string_lists(l):
    return list(filter(lambda x: type(x) == str, l))

print('Only strings: ', get_string_lists(mixed_list))

'''
10. Use reduce to sum all the numbers in the numbers list.
'''
sum_all = reduce(lambda x, y: x + y, numbers)
print('Sum all: ', sum_all)

'''
11. Use reduce to concatenate all the countries and to produce this sentence:
Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
'''
def cool_joint(x, y):
    concat = x + ', ' + y
    if countries.index(y) == len(countries) - 1:
        concat = x + ' and ' + y

    return concat

joint_countries = reduce(cool_joint, countries)
print('Cool joint: ', joint_countries)

'''
12. Declare a function called categorize_countries that returns a list of
countries with some common pattern (you can find the countries list in this
repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
'''
categories = ['land', 'ia', 'island', 'stan']
def categorize_countries():
    def categorize_country(cat, country):
        for c in categories:
            if c in country:
                if c in cat:
                    cat[c].append(country)
                else:
                    cat[c] = [country]
        return cat

    return reduce(categorize_country, all_countries, {})

print('Categorized countries: ', categorize_countries())

'''
13. Create a function returning a dictionary,
where keys stand for starting letters of countries
and values are the number of country names starting with that letter.
'''
def categorize_countries_by_letter():
    def categorize_country(cat, country):
        if country[0] in cat:
            cat[country[0]].append(country)
        else:
            cat[country[0]] = [country]

        return cat

    return reduce(categorize_country, all_countries, {})

print('Categorized countries by letter: ', categorize_countries_by_letter())

'''
14. Declare a get_first_ten_countries function - it returns a list of first
ten countries from the countries.js list in the data folder.
'''
def get_first_ten_countries():
    return all_countries[:10]

print('Ten first countries: ', get_first_ten_countries())

'''
15. Declare a get_last_ten_countries function that
returns the last ten countries in the countries list.
'''
def get_last_ten_countries():
    return all_countries[10:]

print('Last 10 countries: ', get_last_ten_countries())
