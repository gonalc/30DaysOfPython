# Day 6: 30 Days of python programming

## Tuples

### Exercises: Level 1

'''
1. Create an empty tuple
'''
tpl = () # tuple()

'''
2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
'''
brothers = ('Carlos', 'Mateo', 'Adolfo', 'Iñaki', 'Jesús')
sisters = ('Mer', 'Sita', 'Silvia', 'Rocio', 'Candela')
print('Brothers: ', brothers)
print('Sisters: ', sisters)

'''
3. Join brothers and sisters tuples and assign it to siblings
'''
siblings = brothers + sisters
print('Siblings: ', siblings)

'''
4. How many siblings do you have?
'''
print('How many siblings? ', len(siblings))

'''
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
'''
family_members = list(siblings)
family_members.append('Elena')
family_members.append('Javier')
family_members = tuple(family_members)
print('Family members: ', family_members)

print('--------------------------------------------')

### Exercises: Level 2

'''
1. Unpack siblings and parents from family_members
'''
*_siblings, mum, dad = family_members
print('Siblings: ', _siblings)
print('Mum: ', mum)
print('Dad: ', dad)

'''
2. Create fruits, vegetables and animal products tuples.
Join the three tuples and assign it to a variable called food_stuff_tp.
'''
fruits = ('banana', 'strawberry', 'apple', 'pear')
vegetables = ('carrot', 'onion', 'lettuce')
animal_products = ('eggs', 'milk', 'meat')

food_stuff_tp = fruits + vegetables + animal_products
print('Food Stuff: ', food_stuff_tp)

'''
3. Change the about food_stuff_tp tuple to a food_stuff_lt list
'''
food_stuff_lt = list(food_stuff_tp)
print('Food stuff list: ', food_stuff_lt)

'''
4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
'''
middle_item = food_stuff_tp[int(len(food_stuff_tp) / 2) - 1]
print('Middle item: ', middle_item)

'''
5. Slice out the first three items and the last three items from food_staff_lt list
'''
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print('First three: ', first_three)
print('Last three: ', last_three)

'''
6. Delete the food_staff_tp tuple completely
'''
del food_stuff_tp

'''
7. Check if an item exists in tuple:
    * Check if 'Estonia' is a nordic country
    * Check if 'Iceland' is a nordic country
'''
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Is Estonia a nordic country? ', 'Estonia' in nordic_countries)
print('Is Iceland a nordic country? ', 'Iceland' in nordic_countries)