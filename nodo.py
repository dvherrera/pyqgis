#Clase nodo

class Nodo:
    tratado=False
    lista = []

    def __init__(self,nombre):
        self.nom = nombre
        #self.lista = []
    def norte(self):
        return self.nom[4:8]
    def este(self):
        return self.nom[9:13]
    def vecinos(self):
        lista = []
        n = int(self.norte())
        e = int(self.este())
        for n1 in range(n-1,n+2):
            for e1 in range(e-1,e+2):
                if (n1!=n or e1!=e):
                    nom2 = "1kmN"+str(n1)+"E"+str(e1)
                    self.lista.append(nom2)
        return self.lista

    def dime_nombre(self):
        return self.nom

    def tratar(self):
        self.tratado = True
