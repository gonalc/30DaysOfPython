# Day 21: 30 Days of python programming

# Classes and objects

# Exercises: Level 1

'''
1. Python has the module called statistics and we can use this module to
do all the statistical calculations. However, to learn how to make function
and reuse function let us try to develop a program, which calculates the
measure of central tendency of a sample (mean, median, mode) and measure of
variability (range, variance, standard deviation). In addition to those measures,
find the min, max, count, percentile, and frequency distribution of the sample.
You can create a class called Statistics and create all the functions that do
statistical calculations as methods for the Statistics class.
Check the output below.
'''

import statistics

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics():
    def __init__(self):
        self.min_value = 0
        self.max_value = 0
        self._count = 0
        self._sum = 0
        self._mean = 0
        self._median = 0
        self._mode = 0
        self._std = 0
        self._var = 0

    def count(self):
        self._count = len(ages)
        return self._count

    def sum(self):
        self._sum = sum(ages)
        return self._sum
    
    def min(self):
        self.min_value = min(ages)
        return self.min_value
    
    def max(self):
        self.max_value = max(ages)
        return self.max_value

    def range(self):
        return self.max_value - self.min_value

    def mean(self):
        self._mean = statistics.mean(ages)
        return self._mean

    def median(self):
        self._median = statistics.median(ages)
        return self._median

    def mode(self):
        mode_key = statistics.mode(ages)
        mode_count = ages.count(mode_key)
        
        self._mode = { 'mode': mode_key, 'count': mode_count }

        return self._mode

    def std(self):
        self._std = statistics.stdev(ages)
        return self._std

    def var(self):
        self._var = statistics.variance(ages)
        return self._var

    def describe(self):
        print('Count: ', self._count)
        print('Sum: ', self._sum)
        print('Min: ', self.min_value)
        print('Max: ', self.max_value)
        print('Range: ', self.max_value - self.min_value)
        print('Mean: ', self._mean)
        print('Median: ', self._median)
        print('Mode: ', self._mode)
        print('Standard Deviation: ', self._std)
        print('Variance: ', self._var)
        return self

data = Statistics()

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) #  - 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5

print('----- DESCRIBE -----')

data.describe()

# Exercises: Level 2

'''
1. Create a class called PersonAccount.
It has firstname, lastname, incomes, expenses properties
and it has total_income, total_expense, account_info, add_income,
add_expense and account_balance methods. Incomes is a set of
incomes and its description. The same goes for expenses.
'''
class PersonAccount():
    def __init__(self, firstname, lastname, incomes = 0, expenses = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return self.incomes

    def total_expense(self):
        return self.expenses

    def account_info(self):
        print('First name: ', self.firstname)
        print('Last name: ', self.lastname)
        print('Incomes: ', self.incomes)
        print('Expenses: ', self.expenses)

    def add_income(self, new_income):
        self.incomes += new_income

        return self.incomes

    def add_expense(self, new_expense):
        self.expenses += new_expense

        return self.expenses

    def account_balance(self):
        return self.incomes - self.expenses
    
person_account = PersonAccount('Gonzalo', 'Alcaide', 1900, 1800)
print('Income: ', person_account.total_income())
print('Expense: ', person_account.total_expense())
person_account.account_info()
print('Balance before operating: ', person_account.account_balance())
person_account.add_expense(1200)
person_account.add_income(2500)
print('Balance after operating: ', person_account.account_balance())