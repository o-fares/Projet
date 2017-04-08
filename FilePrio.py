# classe FilePrio

from Paire import * # à voir selon le nom du fichier où il y a la classe paire
class FilePrio:
    """classe file d'attente"""
    def __init__(self, fileprio):
        self.fileprio = fileprio

    def estVide(self):
        """renvoie True si la fileprio est vide"""
        return self.fileprio == []

    def afficher2(self):
        """afficher la file prio"""
        for i in range(len(self.fileprio)):
            print([(self.fileprio[i].getElement(), self.fileprio[i].getPriorite())])

    def teteFilePrio(self):
        """Renvoie le premier éléement de la file"""
        assert not self.estVide()
        return self.fileprio[0]

    def queueFilePrio(self):
        """"Supprime le premier element de la file"""
        assert not self.estVide()
        self.fileprio = self.fileprio[1:]

    def ajout(self, paire):
        """Ajoute une paire à la file, la paire est ajouté devant le premier élément avec une priorité inférieure ou égale"""
        if self.fileprio ==  []:
            self.fileprio.insert(0,paire)
        else:
            for i in range(len(self.fileprio)):
                if self.fileprio[i].getPriorite() >= paire.getPriorite():
                    self.fileprio.insert(i, paire)
                    break
                elif paire.getPriorite() > self.fileprio[len(self.fileprio)-1].getPriorite():
                    self.fileprio.insert(len(self.fileprio), paire)
                    
a = FilePrio([Paire("C", 1), Paire("A", 2), Paire("B", 5)])
b = Paire("B", 6)
c = FilePrio([])
c.ajout(b)
c.afficher2()
a.queueFilePrio().afficher()
