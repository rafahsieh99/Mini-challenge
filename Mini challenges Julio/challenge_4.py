grafo = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['5'],
    '4': [],
    '5': []
}


def bfs(grafo, nodo):
    cola = []  
    visitados = set() 

    cola.append(nodo)  
    visitados.add(nodo)  

    while cola:
        nodo_actual = cola.pop(0) 

        print(nodo_actual) 

        for vecino in grafo[nodo_actual]:  
            if vecino not in visitados:  
                visitados.add(vecino)  
                cola.append(vecino)  


print("Recorrido en Anchura (BFS):")
bfs(grafo, '1')
