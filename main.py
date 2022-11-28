import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Abhisek Verma'
email['to'] = 'xxxxxx@xxx.com'
email['subject'] = 'YOU HAVE WON A 1,000,000,000 LOTTERY. CLICK TO CLAIM'

email.set_content('This is just a test email which i sent using python code and nothing more. You have not won any lottery')
# print(email)

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your-email@xxxx.com', 'your-password')
    smtp.send_message(email)

    print('Email Sent')