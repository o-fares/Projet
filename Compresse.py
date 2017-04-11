# module compresse contenant plusieurs fonctions détaillées dans le pdf

from re import *
from Arbre import *
from FilePrio import *
from Paire import *
from Noeud import *

def lireFichier(nomFichier):
    """lit un fichier compris dans le même dossier"""
    fo = open(nomFichier, 'r')
    texte = fo.read()
    return texte

def creerTabFreq(texte):
    """retourne le nombre d'occurences de la lettre char dans texte"""
    listefreq = [0]*52
    maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for chr in texte:
        if chr in maj:
            listefreq[ord(chr)-65] += 1
        elif chr in min:
            listefreq[ord(chr)-71] += 1
    return listefreq

texte = lireFichier("data.txt")

print(creerTabFreq(texte))

def creerFilePriorite(tabfreq):
    """créer la file de priorité composé d'éléments (arbre du caractère, nb occurences)"""
    file = FilePrio([])
    traites = []
    for char in texte:
        A = Arbre(Arbre(None, None, None), Noeud(char), Arbre(None, None, None))
        if ord(char) >= 65 and ord(char)<= 90:
            nbcar = tabfreq[ord(char) - 65]
            if ord(char) not in traites:
                file.ajout(Paire(A, nbcar))
                traites += [ord(char)]
        elif ord(char) >= 97 and ord(char) <= 122:
            nbcar = tabfreq[ord(char) - 71]
            if ord(char) not in traites:
                file.ajout(Paire(A, nbcar))
                traites += [ord(char)]
    return file

def creerArbreCodage(fileprio):
    while not fileprio.estVide():
        Paire1 = fileprio.teteFilePrio()
        fileprio.queueFilePrio()
        if fileprio.estVide():
            return Paire1.getElement()
        Paire2 = fileprio.teteFilePrio()
        fileprio.queueFilePrio()
        new = Paire(Arbre(Paire1.getElement(), Noeud(-1), Paire2.getElement()), Paire1.getPriorite() + Paire2.getPriorite())
        fileprio.ajout(new)
        
file = creerFilePriorite(creerTabFreq(texte))


file.afficher2()
