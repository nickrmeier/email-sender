import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Nick Meier'
email['to'] = 'devonrdavey@gmail.com'
email['subject'] = 'Important Message'

email.set_content(html.substitute(name='Devon'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('nickdummy1938@gmail.com', 'Password3819')
    smtp.send_message(email)
    print('email sent!')
