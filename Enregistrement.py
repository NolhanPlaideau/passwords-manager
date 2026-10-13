import os
import base64
from Utilisation import recall
from Gestionnaire_de_mot_de_passe.Pass import get_fernet


def action_principal():
    while    True:
        choix = input("Quelles actions voulez-vous exécuter Enregistrer / Voir / Quitter ? (E/V/Q) : ").lower()

        if choix == "e":
            account = input("Nom du compte : ")
            password = input("Mot de passe du compte : ")
            save_password(password, account)

        elif choix == "v":
            voir_donnees()

        elif choix == "q":
            print("Fermeture du programme.")
            break

        else:
            print("Choix invalide.")


def save_password(password, account):
    fernet = get_fernet()
    encrypted_password = fernet.encrypt(password.encode())
    encrypted_b64 = base64.b64encode(encrypted_password).decode('utf-8')

    file = "données.txt"
    with open(file, "a", encoding="utf-8") as file:
        file.write(f"{account}:{encrypted_b64}\n")

    print("Mot de passe enregistré avec succès.")


def voir_donnees():
    file = "données.txt"
    if not os.path.exists(file):
        print("Aucune données enregistrées.")
        return

    fernet = get_fernet()

    with open(file, "r", encoding="utf-8") as file:
        for line in file:
            account, encrypted_b64 = line.strip().split(":")
            encrypted_bytes = base64.b64decode(encrypted_b64)
            decrypted = fernet.decrypt(encrypted_bytes).decode()
            print(f"Compte : {account} | Mot de passe : {decrypted}")



if recall():
    action_principal()

elif not recall():
    print("Accès refusé.")





