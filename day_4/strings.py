# Day 4: 30 Days of python programming

## Strings

# 1
'''
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
'''
concat_str = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'

# 2
'''
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
'''
concat_2 = 'Coding' + ' ' + 'For'  + ' ' + 'All'

# 3
'''
Declare a variable named company and assign it to an initial value "Coding For All".
'''
company = "Coding For All"

# 4
'''
Print the variable company using print().
'''
print(company)

# 5
'''
Print the length of the company string using len() method and print()
'''
print(len(company))

# 6
'''
Change all the characters to uppercase letters using upper() method.
'''
company = company.upper()
print('Upper:', company)

# 7
'''
Change all the characters to lowercase letters using lower() method.
'''
company = company.lower()
print('Lower:', company)

# 8
'''
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
'''
company = company.capitalize()
print('Capitalize: ', company)
company = company.title()
print('Title: ', company)
company = company.swapcase()
print('Swap Case: ', company)

# 9
'''
Cut(slice) out the first word of Coding For All string.
'''
coding = 'Coding For All'
print('First word: ', coding[:6])

# 10
'''
Check if Coding For All string contains a word Coding using the method index, find or other methods.
'''
print('Contains \"Coding\": ', coding.index('Coding') >= 0)

# 11
'''
Replace the word coding in the string 'Coding For All' to Python.
'''
print('Replace the word coding for Python: ', coding.replace('Coding', 'Python'))

# 12
'''
Change Python for Everyone to Python for All using the replace method or other methods.
'''
print('Change to Python for everyone: ', coding.replace('All', 'Everyone'))

# 13
'''
Split the string 'Coding For All' using space as the separator (split()).
'''
print('Split: ', coding.split(' '))

# 14
'''
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
'''
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('Separate by comma: ', tech_companies.split(', '))

# 15
'''
What is the character at index 0 in the string Coding For All.
'''
print('Index 0 char: ', coding[0])

# 16
'''
What is the last index of the string Coding For All.
'''
print('Last index char at coding: ', coding[-1])

# 17
'''
What character is at index 10 in "Coding For All" string.
'''
print('Index 10 char at coding: ', coding[10])

# 18
'''
Create an acronym or an abbreviation for the name 'Python For Everyone'.
'''
python_for_everyone = 'Python For Everyone'
print('Acronym: ', python_for_everyone[::-1])

# 19
'''
Create an acronym or an abbreviation for the name 'Coding For All'.
'''
print('Abbreviation: ', coding.strip('l'))

# 20
'''
Use index to determine the position of the first occurrence of C in Coding For All.
'''
print('Index of C: ', coding.index('C'))

# 21
'''
Use index to determine the position of the first occurrence of F in Coding For All.
'''
print('Index of F: ', coding.index('F'))

# 22
'''
Use rfind to determine the position of the last occurrence of l in Coding For All People.
'''
print('RFind: ', coding.rfind('l'))

# 23
'''
Use index or find to find the position of the first occurrence of the word 'because' in the following
sentence: 'You cannot end a sentence with because because because is a conjunction'
'''
sentence = 'You cannot end a sentence with because because because is a conjunction'
print('First because: ', sentence.index('because'))

# 24
'''
Use rindex to find the position of the last occurrence of the word because in the following sentence:
'You cannot end a sentence with because because because is a conjunction'
'''
print('First because: ', sentence.rindex('because'))

# 25
'''
Slice out the phrase 'because because because' in the following sentence:
'You cannot end a sentence with because because because is a conjunction'
'''
start_index = sentence.index('because')
end_index = sentence.rindex('because') + len('because')
print('Sliced because: ', sentence[start_index:end_index])

# 26
'''
Find the position of the first occurrence of the word 'because' in the following sentence:
'You cannot end a sentence with because because because is a conjunction'
'''
print('First because: ', sentence.rindex('because'))

# 27
'''
Slice out the phrase 'because because because' in the following sentence:
'You cannot end a sentence with because because because is a conjunction'
'''
print('Sliced because: ', sentence[start_index:end_index])

# 28
'''
Does ''Coding For All' start with a substring Coding?
'''
print('Starts with Coding? ', coding.index('Coding') == 0)

# 29
'''
Does 'Coding For All' end with a substring coding?
'''
ending = 'coding'
print('Ends with coding? ', coding.endswith(ending))

# 30
'''
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
'''
spaced_coding = '   Coding For All      '
print('Remove spaces: ', spaced_coding.strip())

# 31
'''
Which one of the following variables return True when we use the method isidentifier():
    * 30DaysOfPython
    * thirty_days_of_python
'''
# The second one

# 32
'''
The following list contains the names of some of python libraries:
['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
Join the list with a hash with space string.
'''
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('Joint: ', ' # '.join(python_libraries))

# 33
'''
Use the new line escape sequence to separate the following sentences. 
    * I am enjoying this challenge.
    * I just wonder what is next.
'''
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
'''
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
'''
print('Name\tAge\tCountry\tCity\nGonzalo\t27\tSpain\tMadrid')

# 35
'''
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')

# 36
'''
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

