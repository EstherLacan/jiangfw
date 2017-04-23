# coding:utf-8
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def myMail(from_email,passwd,to_email,project,content):
    SMTPSVR = SMTP('smtp.exmail.qq.com')
    to = ','.join(to_email)
    msg = MIMEMultipart('alternatvie')
    msg['Subject'] = Header(project,"utf-8")
    msg['From'] = r"%s " % Header("info@mhealth365.com","utf-8")
    msg['To'] = to
    content = MIMEText(content,'html', 'utf-8')
    msg.attach(content)
	
    sendSvr = SMTPSVR
    sendSvr.login(from_email,passwd)
    errs = sendSvr.sendmail(from_email,to_email,msg.as_string())
    sendSvr.quit()

if __name__=='__main__':
    from_email = 'info@mhealth365.com'
    passwd = 'mHealth365Dev'
    to_email = ['jiangfengwei_2@126.com']
    project = 'ecg'
    content = '<h1>hello</h1>'
    myMail(from_email,passwd,to_email,project,content)
