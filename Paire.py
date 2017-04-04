# class paire
class Paire():
    #Classe des points du plan
    def __init__(self,a,b):
        self.element = a
        self.priorite = b
        
    def getElement(self):
        #Premier élément de la paire
        return self.element
    
    def getPriorite(self):
        return self.priorite
    
    def setElement(self, x):
        #Modification de la première valeur de la paire
        self.element = x
        
    def setPriorite(self, y):
        #Modification de la deuxième valeur de la paire
        self.priorite = y
    
    def afficher(self):
        """affiche la paire"""
        print((self.getElement(), self.getPriorite()))
