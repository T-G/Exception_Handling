'''
finally keyword is intended to define clean-up actions
that must be executed under all circumstances
'''

# multiple except block
# ex: user input and zero division
def divide_number():
    try:
        # ValueError
        dividend = int(input('Please enter a number to divide: '))
        divisor = int(input('Please enter the divisor: '))

        # ZeroDivision Error
        result = dividend/divisor
    except ValueError:
        print('One/both inputs is/are not numeric...')

    except ZeroDivisionError as e:
        print(e)
    else:
        print(f'Result: {result}')
    finally:
        print('Try block is finished')

# call the divide_number() function
divide_number()


