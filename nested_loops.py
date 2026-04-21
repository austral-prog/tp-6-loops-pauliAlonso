

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    nueva_lista = []
    for sublista in matrix:
        for elemento in sublista:
            nueva_lista.append(elemento)
    return nueva_lista 
   
def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    new_list = []

    for fila in matrix:
        suma = 0 
        for elemento in fila:
            suma += elemento
        new_list.append(suma)
    return new_list 


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
   
    new_list = []
    numero_columnas = len(matrix[0])

    for elemento in range(numero_columnas):
        suma = 0 
        for i in range(len(matrix)):
            suma += matrix[i][elemento]

        new_list.append(suma)
    return new_list 


