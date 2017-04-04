

class Noeud ():
    """Classe pour les noeuds d'un arbre"""
    def __init__(self,valeur):
        self.val = valeur

    def getVal(self):
        """Retourne la valeur de l'étiquette"""
        return self.val

    def setVal(self, a):
        """Affecte à l'étiquette la valeur a """
        self.val = a

