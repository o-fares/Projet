from Noeud import *
class Arbre():
    def __init__(self, A1, n, A2):
        self.fg = A1
        self.fd = A2
        self.racine = n

    def estVide(self):
        """Renvoie True si l'arbre est vide, False sinon"""
        return (self.fd is None) and (self.fg is None) and (self.racine is None)

    def setNoeud(self, A):
        """ change la valeur du noeud"""
        self.racine = A

    def setFd(self, A):
        """change la valeur du fils droit"""
        self.fd = A

    def setFg(self, B):
        """change la valeur du fils gauche"""
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
        """Return True si l'arbre se réduit à une feuille """
        if self.estVide():
            return False
        else :
            return self.getFd().estVide() and self.getFg().estVide()
        
    def ParcoursInfixe(self):
        """on utilise cette fonction pour les tests"""
        texte = ""
        if self.estFeuille():
            texte += str(self.racine.getVal())
            return texte
        else:
            texte += self.getFd().ParcoursInfixe()
            texte += self.getFg().ParcoursInfixe()
            return texte


