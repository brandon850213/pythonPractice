import smtplib  # to create smtp server
from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar to "os.path"

# brummykoenig666@gmail.com
# dummybran123

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Brandon Wang'
email['to'] = 'brandon850213@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')


# setting up the server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('brummykoenig666@gmail.com', 'dummybran123')
    smtp.send_message(email)
    print('all good boss!')
