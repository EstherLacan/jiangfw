#!/usr/bin/python
# Filename: break.py

while True:
    s=raw_input('Enter an integer:')
    if s=='quit':
        break
    print('Length of the string is ', len(s))

print('done')
