import smtplib
from email.mime.text import MIMEText
import json




user=input("Enter your name: ")
email=input("Enter your email address: ")

#Login Credentials
file=open("./config.json",'r')
config=json.load(file)


Msg=f""" Hey {user}.
We Hope you're doing well.
"""

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(config['email'],config['password'])

try:
 s.sendmail('jaiminjagdishjudal@gmail.com',email,Msg)
except Exception as e:
    print(e)


print("Email Sent Successfully")
