import os
from Pass import authentication
from new_mdp import create_password
from Pass import setup_password

DATA_FILE = "données.txt"


def recall():
    if not os.path.exists("données.txt"):
        print("Première utilisation.")
        mdp = create_password()
        setup_password(mdp)
        authentication()
        return True
    else:
        return authentication()
