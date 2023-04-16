# open and read file
def open_file(path):
    try:
        # open
        file = open(path, encoding='UTF-8')
    except FileNotFoundError:
        print('No such file in path: ', path)
    else:
        print(file.read())

# call the open_file() function with wrong file path
# FileNotFoundError
path = 'example10.txt'
#open_file(path)


# get the exception object
def open_file_as_except(path):
    try:
        # open
        file = open(path, encoding='UTF-8')
    except FileNotFoundError as ex:
        print(ex)
    else:
        print(file.read())
# call the open_file_as_except() function in a wrong way
file_name = 'examplee.txt'
#open_file_as_except(file_name)

# Ex:pass
def open_file_as_pass(path):
    try:
        # open
        file = open(path, encoding='UTF-8')
    except FileNotFoundError as ex:
        # Do nothing if the file doesn't exist
        pass
    else:
        print(file.read())

    # code after try-except-else block
    print('Code line after try-except-else')

file_name = 'exampleeff.txt'
open_file_as_pass(file_name)