file = open('output.txt','w')
writing = file.write('Hello, Python!\n')
print('Enter text to write to the file:',writing)
print('Data successfully written to output.txt')
file.close()

file = open('output.txt','a')
appending = file.write ('Learning file handline in Python.')
print ('Enter additional text to append:',appending)
print ('Data successfully appended.')
file.close()


