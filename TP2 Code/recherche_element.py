# 1: recherche d'un élément dans une liste non triée
import time


def recherche_element_non_triee(liste, element):
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return -1


# 2: recherche d'un élément dans une liste triée
def recherche_element_triee(liste, element):
    for i in range(len(liste)):
        if liste[i] == element:
            return i
        if liste[i] > element:
            return -1
    return -1


# 3: recherche dichotomique
def recherche_dichotomique(liste, element):
    debut = 0
    fin = len(liste) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if liste[milieu] == element:
            return milieu
        if liste[milieu] < element:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1


def main():

    # ----------------- Tests -----------------
    liste_triee = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                   51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    list_non_triee = [10, 5, 3, 7, 9, 1, 2, 4, 6, 8, 20, 15, 13, 17, 19, 11, 12, 14, 16, 18, 30, 25, 23, 27, 29, 21, 22, 24, 26, 28, 40, 35, 33, 37, 39, 31, 32, 34, 36, 38, 50, 45, 43, 47, 49, 41, 42, 44, 46,
                      48, 60, 55, 53, 57, 59, 51, 52, 54, 56, 58, 70, 65, 63, 67, 69, 61, 62, 64, 66, 68, 80, 75, 73, 77, 79, 71, 72, 74, 76, 78, 90, 85, 83, 87, 89, 81, 82, 84, 86, 88, 100, 95, 93, 97, 99, 91, 92, 94, 96, 98]

    # calculer le temps d'exécution de la recherche pour chaque fonction
    # 1: recherche d'un élément dans une liste non triée
    debut = time.time()
    recherche_element_non_triee(list_non_triee, 50)
    fin = time.time()
    print("temps d'exécution de la recherche d'un élément dans une liste non triée: ",
          fin - debut, "secondes")
    # ------------------------------

    # 2: recherche d'un élément dans une liste triée
    debut = time.time()
    recherche_element_triee(liste_triee, 50)
    fin = time.time()
    print("temps d'exécution de la recherche d'un élément dans une liste triée: ",
          fin - debut, "secondes")
    # ------------------------------

    # 3: recherche dichotomique
    debut = time.time()
    recherche_dichotomique(liste_triee, 50)
    fin = time.time()
    print("temps d'exécution de la recherche dichotomique: ", fin-debut, "secondes")
    # ------------------------------


if __name__ == "__main__":
    main()

