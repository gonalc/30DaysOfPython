# Day 9: 30 Days of python programming

# Conditionals

# Exercises: Level 1

'''
1. Get user input using input(“Enter your age: ”).
If user is 18 or older, give feedback: You are old enough to drive.
If below 18 give feedback to wait for the missing amount of years. Output: 

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
'''
age = int(input('Enter your age: '))
driving_age = 18

if age >= driving_age:
    print('You are old enough to learn to drive.')
else:
    years_left = abs(age - driving_age)
    print(f'You need {years_left} more years to learn to drive.')


'''
2. Compare the values of my_age and your_age using if … else.
Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
You can use a nested condition to print 'year' for 1 year difference in age,
'years' for bigger differences, and a custom text if my_age = your_age. Output: 

Enter your age: 30
You are 5 years older than me.
'''
your_age = 30
age_difference = your_age - age

if age_difference > 0:
    if abs(age_difference) == 1:
        print('You are one year older than me.')
    else:
        print(f'You are way older than me ({age_difference} years).')
elif age_difference < 0:
    if abs(age_difference) == 1:
        print('You are a year younger than me.')
    else:
        print(f'You are {abs(age_difference)} younger than me.')
else:
    print('Brooo we are the same age old!!')


'''
3. Get two numbers from the user using input prompt.
If a is greater than b return a is greater than b,
if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
'''
number_one = int(input('Enter number one: '))
number_two = int(input('Enter number two: '))

if number_one > number_two:
    print(f'{number_one} is greater than {number_two}')
elif number_one < number_two:
    print(f'{number_one} is lower than {number_two}')
else:
    print(f'{number_one} and {number_two} are equal!!')


# Exercises: Level 2

'''
1. Write a code which gives grade to students according to theirs scores:

90-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
score = int(input('What is your score? '))

if score >= 90:
    print('Your score is A')
elif score >= 70:
    print('Your score is B')
elif score >= 60:
    print('Your score is C')
elif score >= 50:
    print('Your score is D')
else:
    print('Your score is F')

'''
2. Check if the season is Autumn, Winter, Spring or Summer.
If the user input is: September, October or November, the season is Autumn.
December, January or February, the season is Winter. March, April or May,
the season is Spring June, July or August, the season is Summer.
'''
month = input('What month is it now? ').capitalize()

if month == 'December' or month == 'January' or month == 'February':
    print('Winter!')
elif month == 'March' or month == 'April' or month == 'May':
    print('Spring!')
elif month == 'June' or month == 'July' or month == 'August':
    print('Summer!')
elif month == 'September' or month == 'October' or month == 'November':
    print('Autumn!')
else:
    print('Enter a proper month, please.')


'''
3. The following list contains some fruits: 
'''
fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input('Enter a fruit: ').lower()

if new_fruit in fruits:
    print('That fruit already exists on the list.')
else:
    fruits.append(new_fruit)
    print('Updated list: ', fruits)


# Exercises: Level 3

'''
1. Here we have a person dictionary. Feel free to modify it!

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node,
 Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
 Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''
person = {
    'first_name': 'Gonzalo',
    'last_name': 'Alcaide',
    'age': 27,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    middle_skill = person['skills'][int(len(person['skills']) / 2)]
    print('Middle skill: ', middle_skill)

    if 'Python' in person['skills']:
        print('This person knows Python!!')

    if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('This dev is a frontend for sure!!')
    elif len(person['skills']) == 3 and 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('We are talking about a backend guy!!')
    elif 'Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB' in person['skills']:
        print('This is a full stack!!!')
    else:
        print('Unknown title')

if person['is_married'] and person['country'] == 'Finland':
    name = person['first_name']
    last_name = person['last_name']
    country = person['country']
    print(f'{name} {last_name} is married and lives in {country}.')
    