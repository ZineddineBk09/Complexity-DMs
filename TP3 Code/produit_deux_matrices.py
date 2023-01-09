def main():

    # On commence par remplir la premiere matrice A
    row1 = int(input("Entrer le nombre de lignes de la premiere matrice A : "))
    column1 = int(
        input("Entrer le nombre de colonnes de la premiere matrice A : "))
    print("#### Matrice A ####")
    a = []
    for i in range(row1):
        a.append([])  # création d'une ligne vide
        for j in range(column1):
            a[i].append(
                int(input("Entrer l'element A[{}][{}] : ".format(i + 1, j + 1))))

    # Maintenant on va remplir la deuxieme matrice B
    row2 = int(input("Entrer le nombre de lignes de la deuxieme matrice B : "))
    column2 = int(
        input("Entrer le nombre de colonnes de la deuxieme matrice B :"))
    print("#### Matrice B ####")
    b = []
    for i in range(row2):
        b.append([])
        for j in range(column2):
            b[i].append(
                int(input("Entrer l'element B[{}][{}] : ".format(i + 1, j + 1))))

    if column1 == row2:
        # A(n,m) : n = row1, m = column1
        # B(m,p) : m = row2, p = column2

        # On initialise la matrice résultat à 0
        mul = []
        for i in range(row1):
            mul.append([])
            for j in range(column2):
                mul[i].append(0)

        # On fait la multiplication
        for i in range(row1):
            for j in range(column2):
                for k in range(row2):  # as row2 = column1
                    mul[i][j] = mul[i][j] + a[i][k] * b[k][j]

        print("#### Matrice AxB ####")
        for i in range(row1):
            print(" | ", end="")
            for j in range(column2):
                print(mul[i][j], end="\t")
            print("\t| ")
        print()

    else:
        print(
            "La multiplication n'est pas possible car le nombre de colonnes de matrice A n'est != nombre de lignes de matrice B.")

        print("Hello World!")


if __name__ == "__main__":
    main()
