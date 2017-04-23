#! /usr/bin/env python
#coding=utf-8

import socket 
import os 
import sys
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

HOST = '0.0.0.0'
PORT = 18888
BUFSIZE = 1024
ADDR = (HOST,PORT)
MAXL = 10
send_list = ["192.168.1.222","192.168.1.203","127.0.0.1"]

mail_host = 'smtp.exmail.qq.com'
mail_user = 'info@mhealth365.com'
mail_pw = 'mHealth365Dev'


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def judeg_send(addre):
    
    if addre in send_list:
        return 1
    else:
        #print addre
        #print "Err serverIP!"
        return 0


def judeg_message(to, code):

    message = (body)% (to,mail_user,subject,code)
    #print message
    return message


def send_mail(to,code):

    try:
	#print "start mail  ====================="
        #msg = MIMEText("您在掌上心电邮箱注册的验证码是："+code+"，请在5分钟内完成注册认证！", 'plain', 'utf-8')
        #msg = MIMEText("您在掌上心电邮箱注册的验证码是："+code+"，请在5分钟内完成注册认证！<br /><br />verification code is：["+code+"] , please complete registration certification in five minutes in snap_ecg!", 'html', 'utf-8')
        msg = MIMEText("您在掌上心电邮箱注册的验证码是：<span style='color: #ff9900;font-weight: bold;border-bottom-width: 1px; border-bottom-style: dashed; border-bottom-color: rgb(204, 204, 204); z-index: 1; position: static;'>"+code+"</span>，请在5分钟内完成注册认证！<br /><br />verification code is：<span style='color: #ff9900;font-weight: bold;border-bottom-width: 1px; border-bottom-style: dashed; border-bottom-color: rgb(204, 204, 204); z-index: 1; position: static;'>"+code+"</span> , please complete registration certification in five minutes in snap_ecg!", 'html', 'utf-8')
        #msg = MIMEText(nowt + " 检查结果: " + code, 'plain', 'utf-8')
        msg['From'] = _format_addr(u'掌上心电 <%s>' % mail_user)
        msg['To'] = _format_addr('%s' % to)
        msg['Subject'] = Header(u'熙健', 'utf-8').encode()

        server = smtplib.SMTP(mail_host,25)
        #server.set_debuglevel(1)
        server.login(mail_user,mail_pw)
        server.sendmail(mail_user,[to],msg.as_string()) 
        server.quit()
    except smtplib.SMTPConnectError, e:
        print str(e)+"i========================1"
        return


def deal_mess(addre, message):
    #print '=================== deal_mess'

    if judeg_send(addre) == 1:
        pass
    else:
        return

    try:
        to = message.split("/")[0]
        code = message.split("/")[1:]
    except Exception, e: 
        #print str(e)+"2"
        #print "get information fail!"
        return
        # 获取信息失败，返回到隧道继续监听
    try: 
        send_mail(to,code[0])
    except Exception, e: 
        #print str(e)+"3"
        return
        #返回到隧道继续监听
        

def tran_serv():
    
    try:
        servsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	servsock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        servsock.bind((HOST,PORT))
        servsock.listen(MAXL)           
        while(1):
#            print "Waiting ..."
            clisock,addre = servsock.accept()      
#            print "...connected from:",addre
            while(1):
                message = clisock.recv(BUFSIZE)
                if not message:
                    break
                deal_mess(addre[0],message)
        
        clisock.close()
        servsock.close()
    except Exception, e: 
#        print str(e)+"4"
        sys.exit(1)
tran_serv()
