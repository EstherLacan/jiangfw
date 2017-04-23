#A Python Program for List and tuple
import sys

#Make a User-Passwd Login
database = [
            ['admin', 123456],
            ['guest', 123],
            ['Tom', 'tom123'],
            ['Alice', 'alice123']
        ]
username = raw_input("User name: ")
passwd = raw_input("Password: ")
if [username, passwd] in database:
    print "Access granted!"
else:
    print "Access denyed!" 
    sys.exit()

#After login...
x = [3, 5, 2, 8, 9, 10, 56, 99]
print "List X is: "
print x
y = x # x y 用的同一个引用地址
z = x[:]
x.sort()
print "List y is after x.sort(): "
print y
print "List z is after x.sort(): "
print z
y.reverse()
print "List x after y.reverse()"
print x
raw_input("Please Enter for Exit...")
