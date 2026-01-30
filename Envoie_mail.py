import smtplib
from email.message import EmailMessage

def send_code(code):

    email = input("entrer votre addresse mail: ")

    msg = EmailMessage()
    msg["Subject"] = "Code de réinitialisation"
    msg["From"] = "service_access@gmail.com"
    msg["To"] = email
    msg.set_content(f"Voici ton code de réinitialisation : {code}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("service_access@gmail.com", "MOT_DE_PASSE_APPLICATION")
        server.send_message(msg)
    print("Email envoyé avec succès")