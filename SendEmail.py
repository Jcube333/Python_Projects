import smtplib

# for html messages
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.multipart import   MIMEMultipart

# for attachments
from email import encoders
from email.mime.base import MIMEBase
import json




user=input("Enter your name: ")
email=input("Enter your email address: ")

#Login Credentials
file=open("./config.json",'r')
config=json.load(file)


# HTML MESSAGE FORMATTING 

Message = MIMEMultipart()
Message['Subject']='Testing Purposes'
Message['From']='jaiminjagdishjudal@gmail.com'
Message['To']=email

htmlMsg=f'''<html>
<body>
<marquee>This is Jcube Testing the power of Python for {user}</marquee>
</body>
</html>'''

Message.attach(MIMEText(htmlMsg,'html'))

# Adding attachments
cv='Jaimin_2023.pdf'
file2=open('./Jaimin_2023.pdf','rb')
part=MIMEBase('application','octet-stream')
part.set_payload(file2.read())
encoders.encode_base64(part)
part.add_header(
    'Content-Disposition',
    f'''Attachment;filename={cv}''',
)


Message.attach(part)

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(config['email'],config['password'])

try:
 s.sendmail('jaiminjagdishjudal@gmail.com',email,Message.as_string())
except Exception as e:
    print(e)


print("Email Sent Successfully")
