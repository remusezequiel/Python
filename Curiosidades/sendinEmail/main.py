################################################################################
import os
import smtplib
################################################################################
"""
Buscar como funciona os.environ.get y ver porque no anda.

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER'.encode())#"ezequielremus@gmail.com"
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS'.encode())#"197382465e"
"""
################################################################################
EMAIL_ADDRESS = "ezequielremus@gmail.com"
EMAIL_PASSWORD = "197382465e"
EMAIL_AGUS = "m.agustina.morelli@gmail.com"
################################################################################

################################################################################
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    #Encriptacion
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Esto es una prueba usando python'
    body = 'Hola momota, Como estas?\n Estoy haciendo una prueba con python.\nEspero te llegue a vos y no a un x cualquiera jajajaj'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_AGUS, msg)

################################################################################
