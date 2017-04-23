#Sequence's Basic Operation

#index
x = [1, 2, 5, 7, 9, 11, 13, 21, 15, 19, 18]
x[1] = 3
x[-1] = x[-1] -1
print 'Seq X is:\n' + str(x)

#piece
print "x[:] is: " + str(x[:])
print "x[:3] is: " + str(x[:3])
print "x[::2] is: " + str(x[::2])

#add
y = [10, 12, 14]
print 'x+y is: ' + str(x+y)

#multiply
z = 'Python'
print 'z * 5 is:',z*5
