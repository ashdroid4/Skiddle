"""Skiddle starts here."""

# ---------- IMPORTS ----------
from sys import exit

from automate import send_email as send_email_0
from __init__ import cwd, credential, email_default
# -----------------------------

# ----------- CONSTANT -----------
method = dict()
# --------------------------------

# --------------- SCRIPT START ---------------
class Method:
    def set(current:str): 
        method.update({"current": current})
    def get() -> str:
        if not method: return False
        return method["current"]
    def delete():
        del method["current"]

def yon(prompt:str) -> bool:
    for p in range(5):
        answer = (input(prompt)).lower()
        if answer == "yes" or answer == "y": return True
        elif answer == "no" or answer == "n": return False
        else: print("Can not understand what you wrote...")

def setCredential(ask:bool=True):
    if ask:
        credential.update(
        {
            "email": input("Please enter your email address: "),
            "password": input("Please enter your email password: "),
            "server": input("Please enter your SMTP Server Name: "),
            "port": int(input("Please enter the SMTP Port: ")),
        }
    )

    with open(cwd.joinpath("EmailResources", "credential.env"), "w+") as c:
        text = "".join(f"{key} = {credential[key]}\n" for key in credential)
        c.write(text)

def setDefault(ask:bool=True):
    if ask:
        email_default.update(
        {
            "display_name": input("Please enter your Display Name: "),
            "subject": input("Please enter your Subject: "),
        }
    )   
    with open(cwd.joinpath("EmailResources", "default.env"), "w+") as c:
        text = "".join(f"{key} = {email_default[key]}\n" for key in email_default)
        c.write(text)

def send_email(users:list, **kwargs):
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

    from __init__ import credential, email_default

    save = False

    for key in credential:
        if not credential[key]: 
            save = True
            credential[key] = input(f"Please enter {key}: ")

    if save:
        save = yon("Do you want to save these credentials so that you won't have to enter again?(y/n): ")
    if save: setCredential(ask=False)
    
    save = False
    
    for key in email_default:
        if not email_default[key]:
            save = True
            email_default[key] = input(f"Please enter {key}: ")
        
    if save:
        save = yon("Do you want to save these values so that you won't have to enter again?(y/n): ")
    if save:
        setDefault(ask=False)

    send_email_0(users, **credential, **email_default, **kwargs)


def list_getter() -> list:
    print(
        "There are two ways to provide a list of users:\n"
        "1. Type the list here. Emails should be separated by space.\n"
        f"2. Put a text file(.txt) in the '{cwd}' directory. "
        "One line per each email address. Don't put two email addresses on the same line"
    )
    for m in range(5):
        method = input("Which method do you choose?(say in number): ")
        if method.isnumeric(): 
            method = int(method)
            if method == 1 or method == 2: break
            else: print("Choose between 1 or 2")
        else: print("Say in number...")
    
    if method == 1:
        users = input("Cool, type the emails now: ")
        users = users.split(" ")
    
    if method == 2:
        print("Cool. Let's search the directory.")

        user_file = False

        for files in cwd.glob('*.txt'):
            if not files:
                exit(f"No text file found. Put a file in the directory '{cwd}' and restart.")

            user_file = yon(f"Is the file name '{files.name}'?(y/n): ")

            if user_file:
                with open(files) as f:
                    users = ((f.read()).strip()).split('\n')
                    break

        if not user_file:
            exit(f"No text file found. Put a file in the directory '{cwd}' and restart.")
        
    printable = yon("Do you want to check all the email address?(y/n): ")

    if printable: 
        print(f"Found {len(users)} email addresses:\n")
        for user in users: print(user + '\n')
    
    return users

def main():
    from EmailResources.template import body, html

    if not Method.get(): ask = input("> ")

    if ask == "exit": exit()

    if "set cred" in ask: Method.set("set credential")

    if Method.get() == "set credential": setCredential(); Method.delete()

    if "set default" in ask: Method.set("set default")

    if Method.get() == "set default": setDefault(); Method.delete()

    if ask == "send email": Method.set("send email")

    if Method.get() == "send email":

        users = list_getter()
        
        if html and body:
            use = yon(
            "The body of the email and html template already exists. Do you wanna use them?(y/n): "
            )

            if use: send_email(users, body=body, html=html)
            else:
                body = input("Please enter the body of the email: ")
                if yon("Just send the bod without html?"):
                    send_email(users, body=body)
        
        if not body:
            body = input("Please enter the body of the email: ")
            if not html: 
                if yon("Just send the bod without html?"):
                    send_email(users, body=body)
            send_email(users, body=body, html=html)          
        
        Method.delete()


while __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: exit("\nExiting due to Keyboard Interrupt")
# ---------------- SCRIPT END ----------------
