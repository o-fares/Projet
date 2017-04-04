# Author : Mounir Bennadji
# File : Classe Arbre.py

class Noeud:
    """classe des noeuds"""
    def __init__(self, val):
        self.val = val

    def getVal(self):
        """renvoie l'étiquette"""
        return self.val

    def setVal(self, valeur):
        """attribuer une nouvelle valeur à l'étiquette"""
        self.val = valeur

class Arbre():

    def __init__(self, A1, n, A2):
        self.fg = A1
        self.fd = A2
        self.racine =  n

    def estVide(self):
        """Renvoie True si l'arbre est vide, False sinon"""
        return (self.getFd() == None) and (self.getFg() == None) and (self.racine == None)

    def setNoeud(self, A):
        self.racine = A

    def setFd(self, A):
        self.fd = A

    def setFg(self, B):
        self.fg = B

    def getFd(self):
        """Retourne la valeur du fils droit """
        assert (not self.estVide())
        return self.fd

    def getFg(self):
        """Retourne la valeur du fils gauche"""
        assert (not self.estVide())
        return self.fg

    def getRacine(self):
        """Renvoie la racine de l'arbre"""
        assert(not self.estVide())
        return self.racine

    def getValRac(self):
        """Retourne l'étiquette de la racine"""
        assert (not self.estVide())
        return self.racine.getVal()

    def estFeuille(self):
        """Vérifie si un arbre est une feuille"""
        assert not self.estVide()
        return self.fd.estVide() and self.fg.estVide()

