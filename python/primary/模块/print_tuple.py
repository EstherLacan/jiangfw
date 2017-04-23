#!/usr/bin/python
# Filename: print_tuple.py

age = 22
myempty = ()
print(len(myempty))
a1 = ('aa',)
print(len(a1))

a2 = ('abcd')
print(len(a2),a2[3])

name = ('Swaroop')

print ('%s is %d years old' % (name, age))
print ('Why is %s playing with that python?' % name)
