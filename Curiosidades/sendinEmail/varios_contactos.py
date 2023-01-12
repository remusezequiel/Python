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
contacts = ['ezequielremus@gmail.com', 'm.agustina.morelli@gmail.com']
################################################################################

################################################################################
msg = EmailMessage()
msg['Subject'] = 'Enviando pdfs por mail con python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Hola momota\n Decime si te llegan varias foto desde nuestra futura casa')
################################################################################

################################################################################
files = ['casa.jpg', 'casa_dos.jpg','casa_tres.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image',
                        subtype=file_type, filename=f.name)
################################################################################


################################################################################
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    #smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)

################################################################################
