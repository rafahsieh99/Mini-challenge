def eliminar_duplicados(lista):
    return list(set(lista))

lista = [10, 25, 3, 4, 5, 10, 25, 6, 7, 8]
print("Lista original:", lista)

lista_sin_duplicados = eliminar_duplicados(lista)
print("Lista sin duplicados:", lista_sin_duplicados)