import smtplib  # to create smtp server
from email.message import EmailMessage
# brummykoenig666@gmail.com
# dummybran123

email = EmailMessage()
email['from'] = 'Brandon Wang'
email['to'] = 'brandon850213@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('brummykoenig666@gmail.com', 'dummybran123')
    smtp.send_message(email)
    print('all good boss!')
