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

def creerTabFreq2(texte, nbcar):
    """retourne le nombre d'occurences de la lettre chr dans texte"""
    # à utiliser avec nbcar = 256
    listefreq = [0] * nbcar
    for chr in texte:
        listefreq[ord(chr)] += 1
    return listefreq

def creerFilePriorite2(tabfreq, nbcar):
    fileprio= FilePrio([])
    for i in range (nbcar) :
        if tabfreq[i] != [0] :
            char = chr(i)
            A = Arbre(Arbre(None, None, None), Noeud(char), Arbre(None, None, None))
            fileprio.ajout(Paire(A, tabfreq[i]))
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

def tauxcompression(texte):
    """renvoie le taux de compression en %"""
    taux = 100 * len(coderTexte(texte, creerTabCode(creerArbreCodage(creerFilePriorite2(creerTabFreq2(texte, 256), 256)), "", []))) / (8*(len(texte)-1))
    return taux

texte = lireFichier("data.txt")

print(creerTabFreq2(texte, 256))

file = creerFilePriorite2(creerTabFreq2(texte, 256), 256)
file.afficher2()
arbre = creerArbreCodage(file)

tabCode = creerTabCode(arbre,"", [])
for i in range (len(tabCode)) :
    tabCode[i].afficher()

textecode = coderTexte(texte, tabCode)
print(textecode)
print(decoderTexte(textecode, arbre))
print(tauxcompression(texte))
