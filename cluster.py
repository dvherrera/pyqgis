#Clase cluster

class Cluster:
    lista_nodos = []

    def __init__(self,num_cluster):
        self.numero = num_cluster

    def anadir_nodo(self,nodo):
        self.lista_nodos.append(nodo)

    def imprime_nodos(self):
        for kk in self.lista_nodos:
            print(kk.dime_nombre())
    
