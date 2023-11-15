adnMutante=[]

def buscarMutantes(matriz, letrasMutantes):
    for fila in matriz:
        for i in range(len(fila) - letrasMutantes + 1):
            grupo = fila[i:i + letrasMutantes]
            if len(set(grupo)) == 1:
                adnMutante.append("Horizontal")
                print(f"{letrasMutantes} letras repetidas en forma horizontal: {grupo}")

    for j in range(len(matriz[0])):
        for i in range(len(matriz) - letrasMutantes + 1):
            grupo = ''.join(matriz[i + k][j] for k in range(letrasMutantes))
            if len(set(grupo)) == 1:
                adnMutante.append("Vertical")
                print(f"{letrasMutantes} letras repetidas en forma vertical: {grupo}")

    for i in range(len(matriz) - letrasMutantes + 1):
        for j in range(len(matriz[0]) - letrasMutantes + 1):
            grupo = ''.join(matriz[i + k][j + k] for k in range(letrasMutantes))
            if len(set(grupo)) == 1:
                adnMutante.append("Diagonal")
                print(f"{letrasMutantes} letras repetidas en forma diagonal: {grupo}")

    return adnMutante

def matrizUsuario(filas, columnas):
    matrizAdnU= []
    for _ in range(filas):
        fila = input(f"Ingrese las 6 letras (solo A, C, G, T): ").upper()
        while len(fila) != columnas or any(letra not in {'A', 'C', 'G', 'T'} for letra in fila):
            print(f"Error: La fila debe tener exactamente {columnas} letras A, C, G, T.")
            fila = input(f"Ingrese las 6 letras (solo A, C, G, T): ").upper()
        matrizAdnU.append(fila)
    return matrizAdnU

filas = 6
columnas = 6
letrasMutantes=4
matrizAdnU= matrizUsuario(filas, columnas)
resultado = buscarMutantes(matrizAdnU, letrasMutantes)
if len(adnMutante)>1:
    print(f"En la matriz ingresada por el usuario hay dos o más secuencias de {letrasMutantes} letras repetida, el Adn es Mutante")
else:
    print(f"En la matriz ingresada por el usuario hay menos de dos secuencias de {letrasMutantes} letras repetida, el adn no es mutante")
