#A Python Program for List and tuple
import sys

#Make a User-Passwd Login
database = [
            ['admin', 123456],
            ['guest', 123],
            ['tom', 'tom'],
            ['Alice', 'alice123']
        ]

tuplebase = (
            ('admin', 123456),
            ('guest', 123),
            ('tom', 'tom'),
            ('Alice', 'alice123')
        )
dictbase= {'admin':123456,'guest': 123 ,'tom': 'tom',
           'Alice': 'alice123'
            }


username = raw_input("User name: ")
passwd = raw_input("Password: ")
if [username, passwd] in database:
    print ("Access database granted!")
else:
    print ("Access database denyed!")

if (username, passwd) in tuplebase:
    print ("Access tuplebase granted!")
else:
    print ("Access tuplebase denyed!")

    #不能执行
##if {username:passwd} in dictbase:
##    print "Access dictbase granted!"
##else:
##    print "Access dictbase denyed!" 
    


raw_input("Please Enter for Exit...")


