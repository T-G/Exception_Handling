# get the exception object
def open_file(path):
    try:
        # open
        file = open(path, encoding='UTF-8')
    except Exception as ex: # catching all types of exception
        print(ex)
    else:
        print(file.read())
    finally:
        try:
            file.close()
            print('Closing the file')
        except:
            pass
# call the open_file() function in a wrong way
file_name = 'example1.txt'
open_file(file_name)
