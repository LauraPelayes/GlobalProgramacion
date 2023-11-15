# GlobalProgramacion
# Mutantes Python
*Laura Pelayes
*29222785
*laurapelayes82@gmail.com

# El proyecto: ADN Mutante Detector

Este código implementa un detector de secuencias de ADN mutante en una matriz bidimensional. La matriz se puede proporcionar manualmente o ingresar por el usuario. La detección de secuencias mutantes se realiza en las direcciones horizontal, vertical y diagonal.

# Funcionalidades:

buscarMutantes(matriz, letrasMutantes):

Busca secuencias mutantes en una matriz dada.
Identifica y almacena las ubicaciones de las secuencias mutantes en las direcciones horizontal, vertical y diagonal.
Imprime las secuencias mutantes encontradas.

matrizUsuario(filas, columnas):

Permite al usuario ingresar manualmente una matriz de ADN.
Valida que la fila ingresada tenga el número correcto de columnas y contenga solo letras A, C, G o T.

# Ejemplo de Uso:

Tamaño de la matriz: 6x6
Longitud de letras mutantes: 4
El código incluye un ejemplo con matriz generada por el usuario.

# Resultado:

Imprime si hay dos o más secuencias de letras mutantes repetidas en la matriz, indicando que el ADN es mutante.
En caso contrario, indica que no hay suficientes secuencias mutantes en la matriz para ser considerado mutante.
Nota: El código incluye comentarios detallados para facilitar la comprensión del funcionamiento.

# Cómo ejecutarlo:

```
Ingresar al directorio donde está el archivo, abrir la terminal e ingresar por teclado: Mutants.py
Es necesario tener instalado python en el equipo
Ingresar las 6 secuencias de 6 letras pedidas por teclado
Al finalizar, el programa muestra un texto donde indica si el adn es mutante o no


```
# Prueba con matriz ingresada por el usuario:
Ingrese las 6 letras (solo A, C, G, T): AGCTCA
Ingrese las 6 letras (solo A, C, G, T): GATCTG
Ingrese las 6 letras (solo A, C, G, T): TCGCTA
Ingrese las 6 letras (solo A, C, G, T): TCGATC
Ingrese las 6 letras (solo A, C, G, T): AGCATC
Ingrese las 6 letras (solo A, C, G, T): AGCTAT
4 letras repetidas en forma vertical: TTTT
En la matriz ingresada por el usuario hay menos de dos secuencias de 4 letras repetida, el adn no es mutante
