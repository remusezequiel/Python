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
msg['Subject'] = 'Una prueba usando python. Segunda Parte'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_AGUS
msg.set_content('Hola momota\n Decime si te llega una foto desde nuestra futura casa')
################################################################################

################################################################################
with open('casa.jpg', 'rb') as f:
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
