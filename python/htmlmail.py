#!/usr/bin/env python
# -*- coding=utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "pywugw@163.com"
rcpt = "pywugw@163.com"
msg = MIMEMultipart(alternatvie)
msg[Subject] = Header("测试发信","utf-8") #组装信头
msg[From] = r"%s <pywugw@163.com>" % Header("小吴","utf-8") #使用国际化编码
msg[To] = rcpt

html = open(html.tpl).read() #读取HTML模板
html_part = MIMEText(html,html) #实例化为html部分
html_part.set_charset(utf-8) #设置编码
msg.attach(html_part) #绑定到message里

try:
	s = smtplib.SMTP('smtp.exmail.qq.com') #登录SMTP服务器,发信
	s.login(pywugw,*******)
	s.sendmail(sender,rcpt,msg.as_string())
except Exception,e:
	print e 