# class paire
class Paire:
    # Classe des Paires
    def __init__(self, a, b):
        self.element = a
        self.priorite = b

    def getElement(self):
        # Premier élément de la paire
        return self.element

    def getPriorite(self):
        return self.priorite

    def setElement(self, x):
        # Modification de la première valeur de la paire
        self.element = x

    def setPriorite(self, y):
        # Modification de la deuxième valeur de la paire
        self.priorite = y

    def eqPaire(q, p):
        # Renvoie True si les deux paires sont égales, False sinon
        return (q.getElement() == p.getElement()) and (q.getPriorite() == p.getPriorite())

    def afficher(self):
        """affiche la paire"""
        print((self.getElement(), self.getPriorite()))

    def cloner(self):
        return Paire(self.getElement(), self.getPriorite())

