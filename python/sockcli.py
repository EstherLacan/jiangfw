#!/usr/bin/env python
#coding=utf-8

import socket
import os 
import sys

def trans_cli(message):
    HOST = '127.0.0.1'
    PORT = 18888
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    try:
        clisock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clisock.connect(ADDR)
	print 'ccccccccnnnnnnnnneeeeeeeeeeee'
        clisock.sendall(message)
        #print 'Send message: "%s"' % message    
        clisock.close()
    except Exception, e:
        sys.exit(3)
        
def check_arg():
    if len(sys.argv) != 2:
        print "1111"
        sys.exit(1)
    else:
        pass
    try:
        message = sys.argv[1]
        ##判断message是否符合规范 func
        if 2 == len(message.split("/")):
            #print message
            trans_cli(message)
        else:
            print "args ERR"
            sys.exit(1)
    except Exception, e:
	print 'eeeeeeeeeeeeeeee'
        sys.exit(2)    


if __name__ == "__main__":
    check_arg()
