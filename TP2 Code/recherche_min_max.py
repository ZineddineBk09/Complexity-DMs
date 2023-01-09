# 1: approache naïve (min et max)
def min_max_naif(liste):
    global compteur1
    compteur1 = 0

    min = liste[0]
    max = liste[0]
    for i in range(1, len(liste)):
        if liste[i] < min:
            min = liste[i]
            # pour calculer le nombre de comparaisons (question b)
            comparaisons1 += 1
        if liste[i] > max:
            max = liste[i]
            comparaisons1 += 1

        # incrementer le compteur de nombre de d'itérations
        compteur1 += 1
    return min, max
# complexité: O(n)
# nombre de comparaisons: pour chaque iteration, on fait 2 comparaisons => 2n - 2


# 2 approche plus efficace (min et max)
# - On compare par paire les éléments de l’ensemble. On met d’un côté les plus grand éléments (dans les cases paires du tableau) et de l’autre côté les plus petits (dans les cases impaires).
# - On cherche le minimum parmi tous les plus petits éléments.
# - On cherche le maximum parmi tous les plus grands éléments. (si on a un nombre impair d’éléments, il ne faut pas oublier le ne élément qui n’a pas été comparé dans la première phase i. )
def min_max_efficace(liste):
    global compteur2
    compteur2 = 0

    if len(liste) % 2 == 0:
        min = liste[0]
        max = liste[1]
        debut = 2
    else:
        min = liste[0]
        max = liste[0]
        debut = 1
    for i in range(debut, len(liste), 2):
        if liste[i] < liste[i + 1]:
            if liste[i] < min:
                min = liste[i]
            if liste[i + 1] > max:
                max = liste[i + 1]
        else:
            if liste[i + 1] < min:
                min = liste[i + 1]
            if liste[i] > max:
                max = liste[i]

        # incrementer le compteur
        compteur2 += 1

    return min, max

# complexité: O(n/2) = O(n)
# nombre de comparaisons: pour chaque iteration, on fait 3 comparaisons => 3n/2 - 3


# ----------------- Tests -----------------
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

compteur1 = 0  # pour calculer le nombre d'itérations d'algorithme naif
compteur2 = 0  # pour calculer le nombre d'itérations d'algorithme efficace

min1, max1 = min_max_naif(liste)
min2, max2 = min_max_efficace(liste)

print("min1 =", min1, "max1 =", max1, "compteur1 =", compteur1, " iterations")
print("min2 =", min2, "max2 =", max2, "compteur2 =", compteur2, " iterations")
