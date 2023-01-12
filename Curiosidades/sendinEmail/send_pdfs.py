################################################################################
import os
import smtplib
import imghdr
from email.message import EmailMessage
################################################################################

"""
Este ejemplo es para mandar solo una imagen con el mail
"""

################################################################################
EMAIL_ADDRESS = "ezequielremus@gmail.com"
EMAIL_PASSWORD = "197382465e"
EMAIL_AGUS = "m.agustina.morelli@gmail.com"
################################################################################

################################################################################
msg = EmailMessage()
msg['Subject'] = 'Enviando pdfs por mail con python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Me auto mande este mail')
################################################################################

################################################################################
files = ['django-forms.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application',
                        subtype='ocrer-stream', filename=f.name)
################################################################################


################################################################################
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    #smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)

################################################################################
