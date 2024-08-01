# Búsqueda en lista ordenada: Implementa una función de búsqueda binaria que determine si un número está en una lista ordenada de 10 elementos.

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return True  # Se encontro
        elif lista[medio] < objetivo:
            inicio = medio + 1  # Buscar en la mitad derecha
        else:
            fin = medio - 1  # Buscar en la mitad izquierda

    return False  # No se encontro


lista_ordenada = [1, 2, 3, 6, 8, 12, 13, 16, 19, 22]
numero_a_buscar = 16

resultado = busqueda_binaria(lista_ordenada, numero_a_buscar)
print(f"El número {numero_a_buscar} {'está' if resultado else 'no está'} en la lista.")

