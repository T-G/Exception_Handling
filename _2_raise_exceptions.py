'''
Exception Handling Project
There are two type of errors in Python
1. Syntax Error - Design time error - if the code doesn't comply with Python syntax, a sytax error is raised
2. Exceptions - run time errors -
'''

# without exception handling
def raise_exception1():
    # ask user for input
    user_input = input('Please enter an integer: ')
    # if we do not handle the error -> crash
    # ValueError
    num = int(user_input)
    print(num)

# call the function and pass 'asdf'
#raise_exception()
def raise_exception2():
    # ask user for input
    user_input = input('Please enter an integer: ')
    # if we do not handle the error -> crash
    # ValueError

    if not user_input.isdigit():
        raise Exception('Not a number...')
    num = int(user_input)
    print(num)

# call the function and pass 'asdf'
#raise_exception2()


# raise ValueError exception
def raise_defined_exception():
    # ask user for input
    user_input = input('Please enter an integer: ')
    # if we do not handle the error -> crash
    # ValueError

    if not user_input.isdigit():
        raise ValueError('Not a number...')
    num = int(user_input)
    print(num)

# call the function
#raise_defined_exception()

# ASSERTION STATEMENT
# we mainly use asserttion statement for dubbing purposes
def assert_user_input():
    # ask user for input
    user_input = input('Please enter an integer: ')

    # assert the input being integer
    assert int(user_input), ValueError('Not asserted as integer...')

    # user input as integer
    num = int(user_input)
    print(num)

# callthe assert_user_input() function
#assert_user_input()


# DIVISION
def division(n1, n2):
    # assert the divisor not being zero
    # AssertionError -> exception
    assert n2 != 0, 'You cannot divide by zero. - Custom'

    print(n1/n2)

# call the division() function with valid numbers
division(10, 2)
division(45, 0)