import random

# jeu de devinette

nombre_secret = random.randint(1, 10)

print("Devine le nombre entre 1 et 10")

tentative = None

while tentative != nombre_secret:
    tentative = int(input("Ton choix : "))

    if tentative < nombre_secret:
        print("Plus grand")
    elif tentative > nombre_secret:
        print("Plus petit")
    else:
        print("Bravo tu as gagné !")