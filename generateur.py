#------------GENERATEUR DE MOT DE PASSE---------------

import string
import secrets

#1)Recupérer les differents caracteres graces a string e l'inclure dans une liste

caracters= string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation

#2)Demander la longeur du mot de passe à l'utisateur

lenght_pwd= int(input("Quelle longeur voulez vous pour le mot de passe? "))

#3)Melanger et Piocher au hasard grace a secrets

code_hasard=""
for i in range(lenght_pwd):
    code_hasard=code_hasard + secrets.choice(caracters)

#4)Afficher le code suggérer

print(code_hasard)
