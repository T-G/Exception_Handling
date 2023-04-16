'''
try-except block
Python runs the code in the try block,
- If it encounters an error (exception) the code execution will jump to the except block
- Any line in the try block which is under the error line will not be executed
- If no exception occurs, the except clause is skipped and execution of the try statement is finished.

The except block is where you catch the exceptions.
You take the necessary actions in case of an exception in the except block.
'''

# Ex: with no exception handling
def get_squares():
    user_input = input('Enter a number: ')
    num = int(user_input)
    print(num**2)

# call the get_squares() function
#get_squares()

# Ex: with exception handling
def get_squares_try():
    try:
        user_input = input('Enter a number: ')
        num = int(user_input)
        print(num**2)
    except:
        print('Not a number...')

# call the get_squares_try() function
#get_squares_try()

# call the function -> recursion
def get_squares_try_recursion():
    try:
        user_input = input('Enter a number: ')
        num = int(user_input)
        print(num**2)
    except:
        print('Not a number...')
        get_squares_try_recursion() # recursion


# call the get_squares_try_recursion() function
#get_squares_try_recursion()

# Ex: Open a file
# no exception handling
def open_file(path):
    # open
    file = open(path)

    # loop over file line by line
    for line in file:
        print(line.split())

# call the open_file() function with wrong file path
# FileNotFoundError
#path = 'seriees.txt'
#open_file(path)

# file exception handling
def open_file_try(path):
    try:
        # open
        file = open(path)

        # loop over file line by line
        for line in file:
            print(line.split())
    except:
        print('No such file in the path: ', path)

# call the open_file() function with wrong file path
# FileNotFoundError
path = 'seriees.txt'
#open_file_try(path)

# multiple except block
# ex: user input and zero division
def divide_number():
    try:
        # ValueError
        dividend = int(input('Please enter a number to divide: '))
        divisor = int(input('Please enter the divisor: '))

        # ZeroDivision Error
        result = dividend/divisor
        print(result)
    except ValueError:
        print('One/both inputs is/are not numeric...')

    except ZeroDivisionError:
        print('Second number cannot be zero...')

# call the divide_number() function
divide_number()

