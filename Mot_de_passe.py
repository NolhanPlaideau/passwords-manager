import hashlib
import base64
from cryptography.fernet import Fernet
from Test import Key

# Demande à l'utilisateur d'entrer un mot de passe
password = input("Entrez votre mot de passe : ")
# demande nom du compte
Account = input("Entrez le nom de votre compte : ")
# liste pour stocker les mots de passe 
list = []
key = Fernet.generate_key()
fernet = Fernet(key)


def Enregistrer():

    resp = str(input("Voulez-vous enregistrer le mot de passe ? (oui/non) : "))
    if resp == "oui":
        save_password(password, Account)
    if resp == "non":
        print("Mot de passe non enregistré") # Demande d'enregistrement

def save_password(save_password, account):
    list.append("account name = " + account + ", " + "Pass world = " + save_password)

    encrypted = fernet.encrypt(save_password.encode())

    with open("donnees.txt", "a") as fichier:
        fichier.write(f"{account};{encrypted}\n")
    print("Mot de passe enregistré") # Enregistrement du mot de passe hash



_ = str(input("Que voulez-vous faire, Engeristrer ou voir un mot de passe ? (E/V) : "))

if _ == "E":
    Enregistrer()
elif _ == "V":
    print(list[0])



Enregistrer()
print(list)
