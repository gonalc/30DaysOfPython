# Day 5: 30 Days of python programming
from countries import countries

## Lists

### Exercises: Level 1

'''
1. Declare an empty list
'''
from os import remove


lst = [] # list()

'''
2. Declare a list with more than 5 items
'''
players = ['Modric', 'Kroos', 'Casemiro', 'Vinicius', 'Benzema', 'Asensio']
print('Real Madrid players: ', players)

'''
3. Find the length of your list
'''
print('Length: ', len(players))

'''
4. Get the first item, the middle item and the last item of the list
'''
first_item = players[0]
middle_index = int(len(players) / 2)
middle_item = players[middle_index]
last_item = players[-1]
print('First item: ', first_item)
print('Middle item: ', middle_item)
print('Last item: ', last_item)

'''
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
'''
mixed_list = ['Gonzalo', 27, 1.87, 'single', 'Madrid']

'''
6. Declare a list variable named it_companies and assign initial values
Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
'''
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

'''
7. Print the list using print()
'''
print('IT Companies: ', it_companies)

'''
8. Print the number of companies in the list
'''
print('Num of IT companies: ', it_companies)

'''
9. Print the first, middle and last company
'''
first_company = it_companies[0]
middle_index = int(len(it_companies) / 2)
middle_company = it_companies[middle_index]
last_company = it_companies[-1]
print('First company: ', first_company)
print('Middle company: ', middle_company)
print('Last company: ', last_company)

'''
10. Print the list after modifying one of the companies
'''
it_companies[2] = 'Mirror Studio'
print('Modified list: ', it_companies)

'''
11. Add an IT company to it_companies
'''
it_companies.append('Hedyla')
print('Added item to list: ', it_companies)

'''
12. Insert an IT company in the middle of the companies list
'''
it_companies.insert(middle_index, 'Buildspace')
print('Inserted item to list: ', it_companies)

'''
13. Change one of the it_companies names to uppercase (IBM excluded!)
'''
buildspace_index = it_companies.index('Buildspace')
it_companies[buildspace_index] = it_companies[buildspace_index].upper()
print('Uppercased buildspace: ', it_companies)

'''
14. Join the it_companies with a string '#;  '
'''
print('Joint companies: ', '#; '.join(it_companies))

'''
15. Check if a certain company exists in the it_companies list.
'''
print('Is Apple on the list? ', 'Apple' in it_companies)

'''
16. Sort the list using sort() method
'''
it_companies.sort()
print('Sorted: ', it_companies)

'''
17. Reverse the list in descending order using reverse() method
'''
it_companies.reverse()
print('Reversed: ', it_companies)

'''
18. Slice out the first 3 companies from the list
'''
it_companies.sort()
sliced = it_companies[:3]
print('Sliced: ', sliced)

'''
19. Slice out the last 3 companies from the list
'''
last = it_companies[-3:]
print('Last Sliced: ', last)

'''
20. Slice out the middle IT company or companies from the list
'''
mid_index = int(len(it_companies) / 2)
print('Sliced mid company: ', it_companies[mid_index:mid_index + 1])

'''
21. Remove the first IT company from the list
'''
remove_copy = it_companies.copy()
remove_copy.pop(0)
print('List without the first item: ', remove_copy)

'''
22. Remove the middle IT company or companies from the list
'''
remove_copy = it_companies.copy()
del remove_copy[mid_index]
print('Mid removed list: ', remove_copy)

'''
23. Remove the last IT company from the list
'''
remove_copy = it_companies.copy()
remove_copy.pop()
print('List without the last item: ', remove_copy)

'''
24. Remove all IT companies from the list
'''
remove_copy = it_companies.copy()
remove_copy.clear()
print('All removed: ', remove_copy)

'''
25. Destroy the IT companies list
'''
del remove_copy

'''
26. Join the following lists:
* front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
* back_end = ['Node','Express', 'MongoDB']
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print('Full Stack array: ', full_stack)

'''
27. After joining the lists in question 26. Copy the joined list and assign it
to a variable full_stack. Then insert Python and SQL after Redux.
'''
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 1, 'SQL')
print('Updated full stack: ', full_stack)

print('------------------------------------------------------------')

### Exercises: Level 2

'''
1. The following is a list of 10 students ages:
    * Sort the list and find the min and max age
    * Add the min age and the max age again to the list
    * Find the median age (one middle item or two middle items divided by two)
    * Find the average age (sum of all items divided by their number )
    * Find the range of the ages (max minus min)
    * Compare the value of (min - average) and (max - average), use abs() method
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

sorted_ages = sorted(ages)
print('Sorted ages: ', sorted_ages)

min_age = min(ages)
max_age = max(ages)
print('Min age: ', min_age)
print('Max age: ', max_age)

ages.append(min_age)
ages.append(max_age)
print('Appended: ', ages)

median_age = sorted_ages[int(len(sorted_ages) / 2)]
print('Median: ', median_age)

average_age = sum(sorted_ages) / len(sorted_ages)
print('Average: ', average_age)

range_ages = max_age - min_age
print('Range: ', range_ages)

min_average = abs(min_age - average_age)
print('Min Average: ', min_average)

max_average = abs(max_age - average_age)
print('Max Average: ', max_average)

print('-------------------------------------------')

middle_country_index = int(len(countries) / 2)
print('Middle Country: ', countries[middle_country_index])

first_half = countries[:middle_country_index]
second_half = countries[middle_country_index:]

print('Countries lenght: ', len(countries))
print('First half lenght: ', len(first_half))
print('Second half lenght: ', len(second_half))
print('Countries mid index: ', middle_country_index)

more_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = more_countries
print('Scandic: ', scandic)