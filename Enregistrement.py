import os
import base64

from Pass import get_fernet, authentication
from Utilisation import recall
from cryptography.fernet import Fernet


def action_principal():
    while True:
        choix = input(
            "Quelles actions voulez-vous exécuter "
            "Enregistrer / Voir / Quitter ? (E/V/Q) : "
        ).lower().strip()

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
    encrypted_b64 = base64.b64encode(
        encrypted_password
    ).decode("utf-8")

    file_path = "données.txt"

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{account}:{encrypted_b64}\n")

    print("Mot de passe enregistré avec succès.")


def voir_donnees():
    file_path = "données.txt"

    if not os.path.exists(file_path):
        print("Aucune donnée enregistrée.")
        return

    fernet = get_fernet()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or ":" not in line:
                continue

            account, encrypted_b64 = line.split(":", 1)

            try:
                encrypted_bytes = base64.b64decode(encrypted_b64)
                decrypted = fernet.decrypt(
                    encrypted_bytes
                ).decode("utf-8")

                print(
                    f"Compte : {account} | "
                    f"Mot de passe : {decrypted}"
                )

            except Exception:
                print(
                    f"Impossible de déchiffrer le mot de passe "
                    f"du compte : {account}"
                )


if recall():
    action_principal()
else:
    print("Accès refusé.")
