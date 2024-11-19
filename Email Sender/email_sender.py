from email.message import EmailMessage
from email.policy import SMTP
import ssl
import smtplib

email_sender ='mb15lhr@gmail.com'
email_password = 'uuxp xget mxlx vogu'   # use your own password
email_receiver = 'popal42125@cashbn.com' # use any temp email.

subject="hey this email is sent by python :D cool right?"
body="""hello this email is being sent by a code. a python program. just a test as a mini project :D"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtplib:
    smtplib.login(email_sender, email_password)
    smtplib.send_message(em)
    print("Email sent successfully")
