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

def creerTabFreq(texte, char):
    """retourne le nombre d'occurences de la lettre char dans texte"""
    freq = 0
    maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for chr in texte:
        if chr == char:
            if chr in maj:
                freq += 1
            elif chr in min:
                freq += 1
    return freq

texte = lireFichier("data.txt")

print(creerTabFreq(texte, 'e'))

def creerFilePriorite(tabfreq, char):
    """créer la file de priorité composé d'éléments (arbre du caractère, nb occurences)"""
    A = Arbre(None, Noeud(char), None)
    nbcar = tabfreq
    file = FilePrio([])
    file.ajout(Paire(A, nbcar))
    return file

file = creerFilePriorite(creerTabFreq(texte, 'e'), 'e')
print(file)

L = file.afficher2()

A = Arbre(None, None, None)
print(type(A))
