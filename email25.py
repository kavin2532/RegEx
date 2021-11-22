import configparser,string
config = configparser.ConfigParser()                              
config.read('properties.ini')
SERVER = config['EMAILCONFIG']['SERVER']
FROM = config['EMAILCONFIG']['FROM']
USERNAME=config['EMAILCONFIG']['USERNAME']
PASSWORD=config['EMAILCONFIG']['PASSWORD']

SERVER = config['EMAILCONFIG']['SERVER']#"192.168.5.111"
#bcc=["kavin.m@solvedge.in"]
bcc=["kavin.m@solvedge.in","duraibabu.g@solvedge.in"]
FROM = "spark@solvedge.in"#[currentusermail]#config['EMAILCONFIG']['FROM']"spark@solvedge.in"
#TO= ["kavin.m@solvedge.in"]
TO = ["nagarajan.e@solvedge.in","laxmanaa.g@solvedge.in"]

from datetime import date,timedelta

today = str(date.today()-timedelta(days=1))
f = open("C:\\Users\\RDUser\\Desktop\\dailytranscountbefore.txt", "r")
s=f.readlines()
dailytranscountbefore=s[2]
f = open("C:\\Users\\RDUser\\Desktop\\auditcountbefore.txt", "r")
s=f.readlines()
auditcountbefore=s[2]
f = open("C:\\Users\\RDUser\\Desktop\\dailytransdelete.txt", "r")
s1=f.readlines()
s1=s1[1]
s1=s1[1:3]
print(s1)
dailytransdelete=s1
f2 = open("C:\\Users\\RDUser\\Desktop\\auditdelete.txt", "r")
s2=f2.readlines()
s2=s2[1]
s2=s2[1:3]
print(s2,"dfhsghasgg")
auditdelete=s2
f3 = open("C:\\Users\\RDUser\\Desktop\\dailytranscountafter.txt", "r")
s3=f3.readlines()
dailytranscountafter=s3[2]
f = open("C:\\Users\\RDUser\\Desktop\\auditcountafter.txt", "r")
s=f.readlines()
auditcountafter=s[2]
from tabulate import tabulate
from termcolor import colored

#bolditem=(colored('WebService Tables Summary:','green', attrs=['bold']))
bolditem=(('WebService Tables Summary:'))

bolditem2=('Regards,')
bolditem3=('Solvedge Digital-CCP Team.')

# assign data
info = {'Table Name': ['webservise_audit_dailytrans', 'webservise_audit'],
     'Before Delete': [dailytranscountbefore,auditcountbefore], 
     'Deleted count': [dailytransdelete, auditdelete],
     'After delete':[dailytranscountafter,auditcountafter]}

# display table
table_form=(tabulate(info, headers='keys',tablefmt='simple'))
SUBJECT,TEXT="DCCP Transaction Records Delete Alert","Hi All, \n\n"+bolditem+" \n\n Archive Date : Before ("+today+")"+"\n\n"+table_form+"\n\n"+bolditem2+"\n\n"+bolditem3




#"Total rows in web_audit Table : "+totalrow+"\n"+today+" affected rows are:"+affected+"\n Remaining Records :"+remains

message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
import smtplib
server = smtplib.SMTP(SERVER,587)#25 
server.ehlo()
server.starttls()
server.ehlo() 
server.login(config['EMAILCONFIG']['USERNAME'], config['EMAILCONFIG']['PASSWORD'])
server.sendmail(FROM, TO+bcc, message)
server.quit()