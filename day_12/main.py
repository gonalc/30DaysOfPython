# Day 10: 30 Days of python programming
from mymodule import generate_full_name as full_name, sum_nums, gravity as g
from random import random, randint

# Modules

print('Module: ', full_name('Gonzalo', 'Alcaide'))
print('Module sum: ', sum_nums(12, 2))
print('Gravity: ', g)

# Exercises: Level 1

'''
1. Write a function which generates a six digit/character random_user_id.
'''
def random_user_id(size = 6):
    return '#' + str(int(random() * (10 * size))).ljust(size, '0')

print('Random 6 digit number: ', random_user_id())

'''
2. Modify the previous task. Declare a function named user_id_gen_by_user.
It doesn’t take any parameters but it takes two inputs using input().
One of the inputs is the number of characters and the second input is
the number of IDs which are supposed to be generated.
'''
def user_id_gen_by_user():
    num_chars = int(input('Num of characters? '))
    amount_of_ids = int(input('How many ids should I generate? '))

    ids = []
    for n in range(amount_of_ids):
        id = random_user_id(num_chars)
        ids.append(id)
    
    return ids

print('Random ids: ', user_id_gen_by_user())

'''
3. Write a function named rgb_color_gen.
It will generate rgb colors (3 values ranging from 0 to 255 each).
'''
def rgb_color_gen():
    colors = []
    for n in range(3):
        color = randint(0, 255)
        colors.append(str(color))
        
    rgb = ', '.join(colors)
    return f'rgb({rgb})'

print('Random color: ', rgb_color_gen())

# Exercises: Level 2

'''
1. Write a function list_of_hexa_colors which returns any number
of hexadecimal colors in an array (six hexadecimal numbers written after #.
Hexadecimal numeral system is made out of 16 symbols, 0-9 and
first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
'''
def list_of_hexa_colors(amount = 1):
    colors = []
    for x in range(amount):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        color = '#%02X%02X%02X' % (red, green, blue)
        colors.append(color)
    
    return colors

print('COLORS: ', list_of_hexa_colors(4))

'''
2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
'''
def list_of_rgb_colors(amount = 1):
    colors = []
    for x in range(amount):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        color = f'rgb({red}, {green}, {blue})'
        colors.append(color)

    return colors

print('RGB Colors: ', list_of_rgb_colors(3))

'''
3. Write a function generate_colors which can generate any number of hexa or rgb colors.
'''
def generate_colors(type, amount = 1):
    if type == 'hexa':
        return list_of_hexa_colors(amount)
    else:
        return list_of_rgb_colors(amount)
    
print('ANY Color: ', generate_colors('rgb', 2))
print('ANY Color: ', generate_colors('hexa', 3))

# Exercises: Level 3

'''
1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
'''
def shuffle_list(list_to_shuffle):
    shuffled = []
    
    while len(shuffled) != len(list_to_shuffle):
        random_index = randint(0, len(list_to_shuffle) - 1)
        item = list_to_shuffle[random_index]

        if item not in shuffled:
            shuffled.append(item)

    return shuffled

print('Shuffled: ', shuffle_list([1, 2, 3]))

'''
2. Write a function which returns an array of seven random numbers in a range of 0-9.
All the numbers must be unique.
'''
def unique_numbers():
    numbers = []
    for x in range(7):
        num = -1
        while num < 0:
            random_number = randint(0, 9)
            if random_number not in numbers:
                num = random_number
        
        numbers.append(num)
    
    return numbers

print('Seven random numbers: ', unique_numbers())