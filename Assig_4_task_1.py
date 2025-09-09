
try:
    file = open('simple.txt', 'r')
    reading_file = file.read()
    print('Reading file content:')
    print('Line 1 : This is a sample text file')
    print('Line 2 :', reading_file)
    file.close()
except FileNotFoundError:
    print ("Error : The 'simple.txt' was not found.")
