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

def minuscule(char):
    """renvoie True si le caractère est une minuscule"""
    if ord(char)>= 65 and ord(char) <= 90:
        return True
    return False

def majuscule(char):
    """renvoie True si le caractère est une majuscule"""
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    return False

def creerTabFreq(texte, nbcar):
    """retourne le nombre d'occurences de la lettre chr dans texte"""
    # à utiliser avec nbcar = 53
    listefreq = [0]*nbcar
    for chr in texte:
        if minuscule(chr):
            # minuscules
            listefreq[ord(chr) - 65] += 1
        elif majuscule(chr):
            # majuscules
            listefreq[ord(chr) - 71] += 1
        elif ord(chr) == 32:
            # espace
            listefreq[nbcar - 1] += 1
    return listefreq
texte = lireFichier("data.txt")

print(creerTabFreq(texte, 53))

def creerFilePriorite(tabfreq, nbcar):
    """créer la file de priorité composé d'éléments (arbre du caractère, nb occurences)"""
    fileprio = FilePrio([])
    traites = []
    for char in texte:
        A = Arbre(Arbre(None, None, None), Noeud(char), Arbre(None, None, None))
        if minuscule(char):
            freq = tabfreq[ord(char) - 65]
            if ord(char) not in traites:
                fileprio.ajout(Paire(A, freq))
                traites += [ord(char)]
        elif majuscule(char):
            freq = tabfreq[ord(char) - 71]
            if ord(char) not in traites:
                fileprio.ajout(Paire(A, freq))
                traites += [ord(char)]
        elif ord(char) == 32:
            freq = tabfreq[nbcar - 1]
            if ord(char) not in traites:
                fileprio.ajout(Paire(A, freq))
                traites += [ord(char)]
    return fileprio

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
        
def creerTabCode(arbrehufman, code, tabCode) :
    if arbrehufman.estFeuille() :
        return [Paire(arbrehufman.getValRac(), code)]
    else :
        return tabCode + creerTabCode(arbrehufman.getFg(), code + "0", tabCode) + creerTabCode(arbrehufman.getFd(), code + "1", tabCode)
 
def coderTexte(texte, tabcodes):
    """algorithme qui renvoie le texte codé"""
    code = ""
    for char in texte:
        for i in range(len(tabcodes)):
            if tabcodes[i].getElement() == char:
                code += tabcodes[i].getPriorite()
    return code

def decoderTexte(textecode, arbrehufman):
    """renvoie le texte décodé"""
    i = 0
    start = arbrehufman
    decode = ""
    while i != len(textecode):
        courant = textecode[i]
        i += 1
        if courant == '0':
            start2 = start.getFg()
        elif courant == '1':
            start2 = start.getFd()
        else :
            return "Erreur de codage"
        if start2.getValRac() != -1 :
            decode += start2.getValRac()
            start = arbrehufman
        else :
            start = start2
    return decode

file = creerFilePriorite(creerTabFreq(texte, 53), 53)
file.afficher2()
arbre = creerArbreCodage(file)

tabCode = creerTabCode(arbre,"", [])
for i in range (len(tabCode)) :
    tabCode[i].afficher()

textecode = str(coderTexte(texte, tabCode))
print(textecode)
print(decoderTexte(textecode, arbre))
