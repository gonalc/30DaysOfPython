# Day 2: 30 Days of python programming

# Exercise 1
name = 'Gonzalo'
last_name = 'Alcaide'
full_name = name + ' ' + last_name
country = 'Spain'
city = 'Madrid'
age = 27
year = 2022
is_married = False
is_true = True
is_light_on = False

girlfriend, brother, flatmate = 'Mer', 'Carlos', 'Mat'

# Exercise 2
print('name', type(name))
print('last_name', type(last_name))
print('full_name', type(full_name))
print('country', type(country))
print('city', type(city))
print('age', type(age))
print('year', type(year))
print('is_married', type(is_married))
print('is_true', type(is_true))
print('is_light_on', type(is_light_on))
print('girlfriend', type(girlfriend))
print('brother', type(brother))
print('flatmate', type(flatmate))

print('Length of my first name: ', len(name))
print('My last name and first name have the same length: ', len(name) == len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print('total', total)
print('diff', diff)
print('product', product)
print('division', division)
print('remainder', remainder)
print('exp', exp)
print('floor_division', floor_division)

radius = 30
pi = 3.14
area_of_circle = (pi * radius) ** 2
circum_of_circle = 2 * pi * radius

print('area_of_circle', area_of_circle)
print('circum_of_circle', circum_of_circle)

r = float(input('Radius of your circle? '))
area_of_circle = (pi * r) ** 2
circum_of_circle = 2 * pi * r
print('area_of_circle', area_of_circle)
print('circum_of_circle', circum_of_circle)

name = input('What is your name? ')
last_name = input('What is your last name? ')
country = input('Where you from? ')
age = input('How old are you? ')

help('keywords')