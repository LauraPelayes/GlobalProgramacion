# GlobalProgramacion
# Mutantes Python
*Laura Pelayes
*29222785
laurapelayes82@gmail.com

# El proyecto se trata de recorrer una matriz de 6 x 6, con letras entre A, C, G, y T, ingresadas por el usuario, y chequear que no haya más de dos secuencias de 4 letras repetidas de forma vertical, horizontal o diagonal, y si así fuera, devolver un mensaje diciendo que se trata de un adn mutante.

# Lo resolvi primero seteando la matriz yo, verificando con bucles for que haya 4 letras repetidas consecutivas, y guardando un "horizontal", "vertical" o "diagonal" en un array por cada secuencia que fuese encontrada, para después ver si el array contenía dos o más elementos, determinando así si se trataba de un ADN mutante o no y poder devolver el mensaje correspondiente al usuario.

# Se corre de esta manera: primero ingresas las 6 secuencias de 6 letras entre las permitidas, luego de ingresadas, el programa evalúa si hay 4 letras repetidas en dos ocasiones o más, de manera diagonal, horizontal o vertical en la matriz generada, y de acuerdo a esto, muestra el mensaje de "adn mutante" o "adn no mutante" según las ocurrencias de letras repetidas. Esto hace cada bucle de búsqueda: 

# Búsqueda Horizontal: recorre cada fila de la matriz. Dentro de este bucle, hay otro bucle que busca a lo largo de la fila, examinando secuencias de letras con una longitud específica, en este caso, 4. Si encuentra una secuencia donde todas las letras son iguales, agrega la palabra "horizontal" a una lista llamada adnMutante que después se examina para saber si hay más de una palabra guardada, y así mostrar el mensaje de "adn mutante".

# Búsqueda Vertical: recorre cada columna de la matriz. Similar al de búsqueda horizontal, dentro de este bucle hay otro bucle que se desplaza hacia abajo a lo largo de la columna. Examina secuencias de letras con la longitud especificada, 4, y si encuentra una secuencia donde todas las letras son iguales, agrega la palabra "vertical" a la lista adnMutante para ser evaluado al finalizar el recorrido.

# Búsqueda Diagonal: recorre la matriz de manera diagonal. Para cada posición en la matriz, busca las 4 letras iguales en diagonal. Si encuentra una secuencia donde todas las letras son iguales, agrega "diagonal" a la lista adnMutante para ser evaluada al final.

# Al finalizar los recorridos, se evalúa si en la lista adnMutante hay más dos palabras o más guardadas, lo que quiere decir que hay 2 o más secuencias de 4 letras iguales en alguna de las posiciones buscadas, y muestra el mensaje de adn mutante en caso de ser así, y sino, muestra el mensaje de que no hay adn mutante.
```
def buscarMutantes(matriz, letrasMutantes):
    
    # Buscar horizontal
    for fila in matriz:
        for i in range(len(fila) - letrasMutantes + 1):
            grupo = fila[i:i + letrasMutantes]
            if len(set(grupo)) == 1:
                adnMutante.append("Horizontal")
                print(f"{letrasMutantes} letras repetidas en forma horizontal: {grupo}")

    # Buscar vertical
    for j in range(len(matriz[0])):
        for i in range(len(matriz) - letrasMutantes + 1):
            grupo = ''.join(matriz[i + k][j] for k in range(letrasMutantes))
            if len(set(grupo)) == 1:
                adnMutante.append("Vertical")
                print(f"{letrasMutantes} letras repetidas en forma vertical: {grupo}")

    # Buscar diagonal
    for i in range(len(matriz) - letrasMutantes + 1):
        for j in range(len(matriz[0]) - letrasMutantes + 1):
            grupo = ''.join(matriz[i + k][j + k] for k in range(letrasMutantes))
            if len(set(grupo)) == 1:
                adnMutante.append("Diagonal")
                print(f"{letrasMutantes} letras repetidas en forma diagonal: {grupo}")

    return adnMutante

# Ejemplo harcodeado
#matrizAdn = [
#    "ATGCGA",
#    "CAGTGC",
#    "TTATGT",
#    "AGAAGG",
#    "CCCCTA",
#    "TCACTG"
#]


# Ejemplo con matriz generada por usuario
def matrizUsuario(filas, columnas):
    matrizAdnU= []
    for _ in range(filas):
        fila = input(f"Ingrese las 6 letras (solo A, C, G, T): ").upper()
        while len(fila) != columnas or any(letra not in {'A', 'C', 'G', 'T'} for letra in fila):
            print(f"Error: La fila debe tener exactamente {columnas} letras A, C, G, T.")
            fila = input(f"Ingrese las 6 letras (solo A, C, G, T): ").upper()
        matrizAdnU.append(fila)
    return matrizAdnU

# Tamaño matriz
filas = 6
columnas = 6
letrasMutantes=4
# Obtener la matriz del usuario
matrizAdnU= matrizUsuario(filas, columnas)

# Prueba con ambas formas
#letrasMutantes = 4
#resultado = buscarMutantes(matrizAdn, letrasMutantes)
#if len(adnMutante)>1:
#    print("En la matriz harcodeada hay más de una secuencia de Adn repetida, el Adn es Mutante")
#else:
#    print("No hay secuencias de adn mutante")
    
resultado = buscarMutantes(matrizAdnU, letrasMutantes)
if len(adnMutante)>1:
    print(f"En la matriz ingresada por el usuario hay dos o más secuencias de {letrasMutantes} letras repetida, el Adn es Mutante")
else:
    print(f"En la matriz ingresada por el usuario hay menos de dos secuencias de {letrasMutantes} letras repetida, el adn no es mutante")
```
