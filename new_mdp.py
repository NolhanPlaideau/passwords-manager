import os
import secrets
import string



def generation_mot_passe(length=12):
    # Génère un mot de passe sécurisé
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(length))


def create_password():

    if not os.path.exists("secret.key"):
        choix = input(str("Voulez-vous générer un mot de passe ? (oui/non) : ")).lower()

        if choix == "oui":
            mdp = generation_mot_passe()
            print("Mot de passe généré :", mdp)
            return mdp

        elif choix == "non":
            mdp = input("Entrez votre mot de passe, qui permettera l'accés à cette app  : ")
            return mdp

        else:
            print("Veuillez répondre par 'oui' ou 'non'")
            return create_password()
