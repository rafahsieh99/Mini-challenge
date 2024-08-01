grafo = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['5'],
    '4': [],
    '5': []
}

def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()  
    
    if nodo not in visitados:
        print(nodo) 
        visitados.add(nodo)  
        
        for vecino in grafo[nodo]:  
            dfs(grafo, vecino, visitados) 


print("Recorrido en Profundidad (DFS):")
dfs(grafo, '1')
