import hashlib
import base64
from cryptography.fernet import Fernet, InvalidToken
from random import randint
from Envoie_mail import send_code

password = ""  # Variable globale pour stocker le mot de passe

def password_to_key(password):
    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode()).digest()
        )

# Mot de passe choisi
def Generation_mot_passe(password):
    b = 0
    while b < 10 :
        a = str(randint(0,9))
        password = password + a
        b = b + 1
    return password

password = Generation_mot_passe(password)
send_code(password)


def Key():
    # Transformation en clé
    key = password_to_key(password)
    fernet = Fernet(key)

    # Chiffrement
    message = 'Access Granted'
    encrypted = fernet.encrypt(message.encode())
    print("Message chiffré")

    # Demande du mot de passe
    user_password = input("Mot de passe : ")
    key2 = password_to_key(user_password)
    fernet2 = Fernet(key2)

    # Déchiffrement
    try:
        decrypted = fernet2.decrypt(encrypted).decode()
        print(decrypted)
        return True
    except InvalidToken:
        print("Mot de passe incorrect !")
        return False


# Utilisation correcte
resp = Key()

if resp == True:
    print("OK, accès autorisé")
else:
    print("Accès refusé")
