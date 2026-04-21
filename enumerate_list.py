

def enumerate_list(lst):
    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """
    nueva_lista = []
    index = 0
    for item in lst:
        if item:
            nueva_lista.append(f"{index}. {item}") 
            index += 1
    return nueva_lista


def enumerate_backwards(lst):
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """
    tercer_lista = []
    index = 0 

    for item in lst:
        if item: 
           inverso = item[::-1]
           tercer_lista.append(f"{index}. {inverso}")
           index += 1
           
    return tercer_lista 

