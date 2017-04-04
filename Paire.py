# class paire
class Paire():
    #Classe des points du plan
    def __init__(self,a,b):
        self.elemnent = a
        self.priorité = b
    def getX(self):
        #Première élément de la paire
        return self.element
    def getY(self):
        return self.priorité
    def setX(self,x):
        #Modification de la première valeur de la paire
        self.element = x
    def setY(self,y):
        #Modification de la deuxième valeur de la paire
        self.priorité = y
    def eqpaire(q,p):
        #Renvoie True si les deux paires sont égales, False sinon
        return (q.getX() == p.getX()) and (q.getY() == p.getY())
    def afficher(self):
        return (self.getX(), self.getY())
    def cloner(self):
        return (Paire(self.getX(),self.getY()))
