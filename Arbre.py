# Author : Mounir Bennadji
# File : Classe Arbre.py

from Noeud import *

class Arbre():

    def __init__(self, A1, n, A2):
        self.fg = A1
        self.fd = A2
        self.racine =  n

    def estVide(self):
        """Renvoie True si l'arbre est vide, False sinon"""
        return (self.fd == None) and (self.fg == None) and (self.racine == None)

    def setNoeud(self,A):
        self.racine = A

    def setFd(self,A):
        self.fd = A

    def setFg(self,B):
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
        if self.estVide():
            return False
        else :
            return self.fd.estVide() and self.fg.estVide()

