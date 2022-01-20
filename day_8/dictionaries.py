# Day 8: 30 Days of python programming

## Dictionaries

### Exercises: Level 1

'''
1. Create an empty dictionary called dog
'''
dog = {} # dict()

'''
2. Add name, color, breed, legs, age to the dog dictionary
'''
dog['name'] = 'Balu'
dog['color'] = 'Dark'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 12
print('Updated dog: ', dog)

'''
3. Create a student dictionary and add first_name, last_name,
gender, age, marital status, skills, country, city and address as keys for the dictionary
'''
student = dict()
student['first_name'] = 'Gonzalo'
student['last_name'] = 'Alcaide'
student['gender'] = 'Male'
student['age'] = 27
student['marital_status'] = 'In a relationship'
student['skills'] = ['JavaScript', 'React', 'SQL', 'NodeJS', 'MongoDB']
student['country'] = 'Spain'
student['city'] = 'Madrid'
student['address'] = 'Calle Falsa 123'
print('Student: ', student)

'''
4. Get the length of the student dictionary
'''
print('Student length: ', len(student))

'''
5. Get the value of skills and check the data type, it should be a list
'''
skills = student['skills']
print('Skills: ', skills)
print('Skills type: ', type(skills))

'''
6. Modify the skills values by adding one or two skills
'''
student['skills'].append('React Native')
print('Updated skills: ', student)

'''
7. Get the dictionary keys as a list
'''
student_keys = student.keys()
print('Student keys: ', student_keys)

'''
8. Get the dictionary values as a list
'''
student_values = student.values()
print('Student values: ', student_values)

'''
9. Change the dictionary to a list of tuples using items() method
'''
list_of_tuples = student.items()
print('List of tuples: ', list_of_tuples)

'''
10. Delete one of the items in the dictionary
'''
student.pop('address')
print('Keys after deletion: ', student.keys())

'''
11. Delete one of the dictionaries
'''
del student
