"""
This script helps to send emails.
"""

# ---------- IMPORTS ----------
import smtplib, ssl
from sys import exit
from time import sleep

from email.message import EmailMessage
from email.headerregistry import Address
# -----------------------------

# --------------- SCRIPT START ---------------
def login(email:str = ..., password:str = ..., server:str=..., port:int=...):
    """
    This function will help login to your email account.\n
    The keyword arguments are:
        - email: The email address you want to login with.
        - password: The password of the email address you want to login with.\n
        - server: The SMTP server name.
        - port: The SMTP port.
    All the keyword arguments are required.
    """
    if not email and not password: exit("Email address and password not given!!")
    if not email: exit("Email address not given!!")
    if not password: exit("Email password not given!!")

    print('Trying to login...')

    context = ssl.create_default_context()

    smtp = smtplib.SMTP(server, int(port))
    smtp.starttls(context=context)
    smtp.login(email, password)

    print('Logged in!')
    return smtp

def send_email(
    users:list, email:str=..., password:str=..., 
    server:str=..., port:int=..., display_name:str=..., 
    subject:str=..., body:str=..., html:str=...
):
    """
    This function will login to your email and send emails to users.\n
    The arguments are:
        - users: The list of email address to whom the email is to be sent. The 'To'.\n
    The keyword arguments are:
        - email: The email address you want to login with.
        - password: The password of the email you want to login with.
        - server: The SMTP server name.
        - port: The SMTP port.
        - display_name: The display name for the email address.
        - subject: The subject for the email to be sent.
        - body: The body of the email to be sent.
        - html: If you have a html code for the email, feel free to pass it as a string.\n
    All the keyword arguments are required.
    """

    smtp = login(email=email, password=password, server=server, port=port)

    for user in users:
        from_address = Address(display_name=display_name, addr_spec=email)
        to_address = Address(addr_spec=user)

        message = EmailMessage()
        message['From'] = from_address
        message['Subject'] = subject
        message['To'] = to_address

        message.set_content(body)
        if html: message.add_alternative(html, subtype='html')

        try:
            smtp.send_message(message, from_addr=email, to_addrs=user)
            print(f'Email sent to {user}!')
        except Exception as error:
            print(f'Error!\n{str(type(error).__name__)}: {error}')
        sleep(2)
    
    smtp.quit()
# ---------------- SCRIPT END ----------------
    
