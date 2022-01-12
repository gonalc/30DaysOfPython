# Day 3: 30 Days of python programming

# Exercise 1, 2, 3
age = 27
height = 1.87
complex = 4 + 18j

# Exercise 4
triangle_base = float(input('Enter triangle base: '))
triangle_height = float(input('Enter triangle height: '))
print('Triangle area is: ', (triangle_base * triangle_height) / 2)

# Exercise 5
perimeter = float(input('Enter side A of a triangle: '))
perimeter += float(input('Enter side B of a triangle: '))
perimeter += float(input('Enter side C of a triangle: '))
print('The perimeter of the triangle is: ', perimeter)

# Exercise 6
rectangle_base = float(input('Enter rectangule base: '))
rectangle_height = float(input('Enter rectangule height: '))
rectangle_perimeter = (rectangle_height + rectangle_base) * 2
rectangle_area = rectangle_base * rectangle_height
print('Reactangle perimeter is: ', rectangle_perimeter)
print('Reactangle area is: ', rectangle_area)

# Exercise 7
radius = float(input('Tell me the circle radius: '))
pi = 3.14
circumference = 2 * pi * radius
circle_area = (pi * radius) ** 2
print('Circumference: ', circumference)
print('Circle area: ', circle_area)

# Exercise 8 -> I don't understant slop

# Exercise 9 - x(2, 2) - y(6, 10)
euclidean = (((6 - 2) ** 2) + ((10 - 2) ** 2)) // 2
print('Euclidean distance: ', euclidean)

# Exercise 10 -> Can't compare slops
'''
Compare the slopes in tasks 8 and 9.
'''

# Exercise 11
'''
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
'''
x = float(input('Enter X: ')) # If -3 Y would be 0
y = (x ** 2) + 6 * x + 9
print('Y is: ', y)

# Exercise 12
'''
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
'''
python_length = len('python')
dragon_length = len('dragon')
print('Falsy comparison: ', python_length != dragon_length)

# Exercise 13
'''
Use and operator to check if 'on' is found in both 'python' and 'dragon'
'''
on_python = 'on' in 'python'
on_dragon = 'on' in 'dragon'
print('on is found in both python and dragon: ', on_python and on_dragon)

# Exercise 14
'''
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
'''
sentence = 'I hope this course is not full of jargon'
print('Is jargon in the sentence? ', 'jargon' in sentence)

# Exercise 15
'''
There is no 'on' in both dragon and python
'''
print('on is NOT found in both python and dragon: ', not(on_python and on_dragon))

# Exercise 16
'''
Find the length of the text python and convert the value to float and convert it to string
'''
result_string = str(float(len('python')))
print('Length to Float to String: ', result_string)

# Exercise 17
'''
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
'''
num = float(input('Enter a number: '))
is_even = num % 2 == 0
print(num, ' is even: ', is_even)

# Exercise 18
'''
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
'''
int = int(2.7)
floor = 7 // 3
print('Is the floor equal tot he int? ', int == floor)

# Exercise 19
'''
Check if type of '10' is equal to type of 10
'''
print("type of '10' equal to 10: ", type('10') == type(10))

# Exercise 20
'''
Check if int('9.8') is equal to 10
'''
# print('Exercise 20: ', int('9.8') == 10)
print('Exercise 20: ', float('9.8') == 10)

# Exercise 21
'''
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
'''
hours = float(input('Enter hours: '))
pay_rate = float(input('Rate per hour: '))
print('Your weekly earning is: ', hours * pay_rate)

# Exercise 22
'''
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
'''
years = float(input('How old are you? '))
print('You have lived for ', years * 365 * 24 * 60 * 60, 'seconds')

# Exercise 23
'''
Write a Python script that displays the following table:

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
for x in range(5):
    num = x + 1
    print(num, 1, num, num ** 2, num ** 3)