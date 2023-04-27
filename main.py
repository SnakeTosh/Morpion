plateau = [" " for _ in range(9)]


def afficherPlateau(p, gagnant=None):
    print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
    print("---+---+---")
    print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
    print("---+---+---")
    print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")
    if gagnant:
        print("""* Partie terminée : le joueur {0} a gagné. *""".format(gagnant))


def morpion():
    joueur = "X"
    tour = 0

    while True:
        afficherPlateau(plateau)
        print("> Tour du joueur " + joueur + ". Entrez un nombre de 1 à 9.")

        move = int(input())

        if move > 9 :
            print("Réponse invalide, veuillez saisir un chiffre compris entre 0 et 9 inclus")
            continue
        if move < 1 :
            print("Réponse invalide, veuillez saisir un chiffre compris entre 0 et 9 inclus")
            continue
        else :
            move = move - 1

        if plateau[move] == " ":
            plateau[move] = joueur
            tour += 1
        else:
            print("! Case déjà occupée, choisissez-en une autre.")
            continue

        if plateau[0] == plateau[1] == plateau[2] != " " \
        or plateau[3] == plateau[4] == plateau[5] != " " \
        or plateau[6] == plateau[7] == plateau[8] != " " \
        or plateau[0] == plateau[3] == plateau[6] != " " \
        or plateau[1] == plateau[4] == plateau[7] != " " \
        or plateau[2] == plateau[5] == plateau[8] != " " \
        or plateau[0] == plateau[4] == plateau[8] != " " \
        or plateau[2] == plateau[4] == plateau[6] != " ":
            afficherPlateau(plateau, joueur)
            return tour

        if tour == 9:
            print("Égalité")
            break

        joueur = "O" if joueur == "X" else "X"

morpion()