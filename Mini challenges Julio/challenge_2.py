# Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros utilizando cualquier método de ordenamiento que prefieras
#  (por ejemplo, burbuja, inserción, selección).

def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


lista_desordenada = [100, 120, 50, 20, 2]
lista_ordenada = ordenar_burbuja(lista_desordenada)

print("Lista ordenada:", lista_ordenada)
