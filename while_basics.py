def countdown(n):
    """Retorna una lista con la cuenta regresiva desde n 
    hasta 0. Si n < 0, retorna []."""
    if n < 0:
        return []

    result = []
    i = n

    while i >= 0:
        result.append(i)
        i -= 1
    return result


def double_until(limit):
    """
    Comenzando desde 1, va duplicando el valor y agrega cada uno
    a una lista mientras sea menor o igual a limit.
    Si limit < 1, retorna una lista vacia.

    Ejemplo: double_until(10) -> [1, 2, 4, 8]
    Ejemplo: double_until(1) -> [1]
    Ejemplo: double_until(0) -> []
    """

    if limit < 1:
        return []
    result = []
    i = 1

    while i <= limit:
        result.append(i)
        i *= 2
    return result 
    