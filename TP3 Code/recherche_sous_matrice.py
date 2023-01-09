# 1) En supposant que les éléments de A et B ne sont pas triés, écrire une fonction sousMat1 qui retrouve B dans A. Evaluez sa complexité temporelle théorique.


def sous_matrice_naive(A, B):
    count = 0

    # A[n][m] : n = lignes, m = colonnes
    # B[n'][m'] : n' = lignes, m' = colonnes
    n = len(A)
    m = len(A[0])
    n_prime = len(B)
    m_prime = len(B[0])

    for i in range(0, n):  # n
        for j in range(0, m):  # m
            if A[i][j] == B[0][0]:
                for k in range(0, n_prime):  # n'
                    for l in range(0, m_prime):  # m'
                        if A[i + k][j + l] == B[k][l]:
                            print("B[{}][{}] trouvé à A[{}][{}]".format(
                                k, l, i + k, j + l))
                            count += 1  # compte le nombre d'éléments de B trouvés

    if count == 9:  # si cpt == n' x m' => tous  les éléments de B ont été trouvés
        return 1
    else:
        return 0
# la complexité temporelle est de O(n x m x n' x m') = O(n^2 x m^2)


# 2) En supposant que chacune des lignes de A et B est triée par ordre croissant , écrire une fonction sousMat2 non naïve de complexité minimale pour trouver B dans A.
def sous_matrice_non_naive_avec_tri(A, B):
    count = 0

    # A[n][m] : n = lignes, m = colonnes
    # B[n'][m'] : n' = lignes, m' = colonnes
    n = len(A)
    m = len(A[0])
    n_prime = len(B)
    m_prime = len(B[0])

    for i in range(0, n):  # n
        # trouver le premier élément de B dans A en utilisant la recherche dichotomique (si trouvé, vérifier si le reste des éléments sont dans le même ordre que dans B)
        # On utilise la meme fct de recherche dichotomique  de TP2

        j = recherche_dichotomique(A[i], B[0][0])
        if j != -1:
            for k in range(0, n_prime):
                for l in range(0, m_prime):
                    if A[i + k][j + l] == B[k][l]:
                        print("B[{}][{}] trouvé à A[{}][{}]".format(
                            k, l, i + k, j + l))
                        count += 1

    if count == 9:  # si cpt == n' x m' => tous  les éléments de B ont été trouvés
        return 1
    else:
        return 0

# la complexité temporelle est de O(n x log(m) x n' x m') = O(n x log(m) x n' x m')


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


# ----------------- Tests -----------------
A = [[21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
     [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
     [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
     [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
     [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
     [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
     [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
     [81, 82, 83, 84, 85, 86, 87, 88, 89, 90]]

B = [[68, 69, 70],
     [78, 79, 80],
     [88, 89, 90]]

# Algo naïf
print("Algo naïf")
if (sous_matrice_naive(A, B)):
    print("B est une sous matrice de A")
else:
    print("B n'est pas une sous matrice de A")

# Algo non naïf
print("Algo non naïf")
if (sous_matrice_non_naive_avec_tri(A, B)):
    print("B est une sous matrice de A")
else:
    print("B n'est pas une sous matrice de A")
