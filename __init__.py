"""
This is the init file of Skiddle
"""

# ---------- IMPORTS ----------
from os import getenv, environ
from pathlib import Path
from dotenv import load_dotenv
# -----------------------------

cwd = (Path(__file__).parent).absolute()

credentialPath = cwd.joinpath('EmailResources', 'credential.env')
email_defaultPath = cwd.joinpath('EmailResources', 'default.env')

if credentialPath.exists(): load_dotenv(credentialPath)
if email_defaultPath.exists(): load_dotenv(email_defaultPath)

credential = {
    "email": getenv("email"),
    "password": getenv("password"),
    "server": getenv("server"),
    "port": getenv("port"),
}

email_default = {
    "display_name": getenv("display_name"),
    "subject": getenv("subject"),
}