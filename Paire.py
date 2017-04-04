# class paire
class Paire():
    #Classe des points du plan
    def __init__(self,a,b):
        self.element = a
        self.priorite = b
        
    def getX(self):
        #Premier élément de la paire
        return self.element
    
    def getY(self):
        return self.priorite
    
    def setX(self, x):
        #Modification de la première valeur de la paire
        self.element = x
        
    def setY(self, y):
        #Modification de la deuxième valeur de la paire
        self.priorite = y
        
    def eqPaire(q, p):
        #Renvoie True si les deux paires sont égales, False sinon
        return (q.getX() == p.getX()) and (q.getY() == p.getY())
    
    def afficher(self):
        """affiche la paire"""
        return (self.getX(), self.getY())
    
    def cloner(self):
        return (Paire(self.getX(),self.getY()))
