# Day 17: 30 Days of python programming

# Exceptions

# Exercises: Level 1

'''
1. Unpack the first five countries and store them in a variable nordic_countries,
store Estonia and Russia in es, and ru respectively.
'''
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names
print('Nordic countries: ', nordic_countries)
print('Es: ', es)
print('Ru: ', ru)