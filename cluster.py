#Clase cluster

class Cluster:
    lista_nodos = []
    lista_nombre_nodos = []
    lista_nodos_externos = []
    lista_nodos_internos = []

    def __init__(self,num_cluster):
        self.numero = num_cluster

    def anadir_nodo(self,nodo):
        self.lista_nodos.append(nodo)

    def imprime_nodos(self):
        for kk in self.lista_nodos:
            print(kk.dime_nombre())
    
    def coloca_nodos(self):
        lista_comprobacion = self.nombre_lista_nodos()
        for kk in self.lista_nodos:
            valor=True
            for m in kk.vecinos():
                if m not in self.lista_nodos:
                    valor=False
            if valor == True:
                    self.lista_nodos_internos.append(kk)
            else:
                    self.lista_nodos_externos.append(kk)

    def nombre_lista_nodos():
        for kk in self.lista_nodos;
            self.lista_nombre_nodos.append(kk.dime_nombre())
        return self.lista_nombre_nodos
