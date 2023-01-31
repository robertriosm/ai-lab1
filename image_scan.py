from numpy import array


def check_bit(bit:array):
    """
    funcion para revisar si un pixel es blanco=1, negro=0, rojo=2 o verde=3
    """
    # revisamos si en negro
    if bit[0] < 70 and bit[1] < 70 and bit[2] < 70:
        return 0 # 0 es pared

    # revisamos si es blanco
    if bit[0] > 250 and bit[1] > 250 and bit[2] > 250:
        return 1 # es camino
    
    # revisamos si es rojo inicio
    if bit[0] > 200 and bit[1] < 120 and bit[2] < 120:
        return 2 # inicio
    
    # revisamos si es goal verde
    if bit[0] < 120 and bit[1] > 200 and bit[2] < 120:
        return 3 # goal
    
    # si no es ninguno, se asume pared
    return 0


