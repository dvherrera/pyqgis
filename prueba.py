# prueba
from nodo import Nodo
from cluster import Cluster

nodo1 = Nodo("1kmN1234E1234")
listanombrenodos = nodo1.vecinos()
#print(listanombrenodos)
#print
#print
#listanodos1 = [nodo1]
#for kk in listanombrenodos:
#    listanodos1.append(Nodo(kk))

#for kk in listanodos1:
#    kk.dime_nombre()

cluster1 = Cluster(2)

cluster1.anadir_nodo(nodo1)
for kk in listanombrenodos:
    cluster1.anadir_nodo(Nodo(kk))

cluster1.anadir_nodo(Nodo("1kmN2222E2222"))


cluster1.imprime_nodos()
print(cluster1.lista_nodos_externos)
print(cluster1.lista_nodos_internos)

cluster1.coloca_nodos()
for kk in cluster1.lista_nodos_externos:
    print (kk.dime_nombre())
print
print
for kk in cluster1.lista_nodos_internos:
    print (kk.dime_nombre())


