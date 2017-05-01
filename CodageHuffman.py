# Fichier regroupant l'ensemble du code utilisé pour le codage Huffman

#########################################################
#                                                       #
# "Classes des Paires,Noeud, Arbre, Files prioritaires" #
#                                                       #
#########################################################


# Classe pour les noeuds

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

#########################################################

# Classe des Paires

class Paire:
    # Classe des points du plan
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

#####################################################################

# Classe des Arbres

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
        """Return True si l'arbre se réduit à une feuille """
        if self.estVide():
            return False
        else:
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

####################################################################

# Classe des file prioritaires

from Arbre import *
from Paire import *

class FilePrio:
    def __init__(self, fileprio):
        self.fileprio = fileprio

    def estVide(self):
        """renvoie True si la fileprio est vide,False sinon"""
        return self.fileprio == []

    def afficher2(self):
        """afficher la file prio"""
        for i in range(len(self.fileprio)):
            if type(self.fileprio[i].getElement()) == Arbre:
                print([(self.fileprio[i].getElement().getFg(), self.fileprio[i].getElement().getValRac(),
                        self.fileprio[i].getElement().getFd()), self.fileprio[i].getPriorite()])
            else:
                print([(self.fileprio[i].getElement(), self.fileprio[i].getPriorite())])

    def teteFilePrio(self):
        """Renvoie le premier élement de la file"""
        assert (not self.estVide())
        return self.fileprio[0]

    def queueFilePrio(self):
        """Supprime le premier élément de la file """
        assert (not self.estVide())
        self.fileprio = self.fileprio[1:]

    def ajout(self, paire):
        """Ajoute une paire à la file, la paire est ajouté devant le premier élément avec une priorité inférieure
        ou égale"""
        if self.fileprio ==  []:
            self.fileprio.insert(0,paire)
        else:
            for i in range(len(self.fileprio)):
                if self.fileprio[i].getPriorite() >= paire.getPriorite():
                    self.fileprio.insert(i, paire)
                    break
                elif paire.getPriorite() > self.fileprio[len(self.fileprio)-1].getPriorite():
                    self.fileprio.insert(len(self.fileprio), paire)



###############################################################
#                                                             #
# Classe de tests pour les classes Paire,Arbre,FilePrio       #
#                                                             #
###############################################################



# Classe de test de la classe Paire

import unittest
from Paire import *


class TestPaire(unittest.TestCase):

    def testGetElement(self):
        a = Paire(1, 2)
        expected = 1
        value = a.getElement()
        self.assertTrue(value == expected)

    def testGetPriorite(self):
        b = Paire(6, 4)
        expected = 6
        value = b.getElement()
        self.assertTrue(value == expected)

    def testEqPaire(self):
        a = Paire(6, 3)
        b = Paire(6, 3)
        self.assertTrue(a.eqPaire(b))

    def testSetElement(self):
        b = Paire(2, 3)
        b.setElement(6)
        value = b.element
        expected = 6
        self.assertTrue(value == expected)

    def testSetPriorite(self):
        m = Paire(12, 14)
        m.setPriorite(3)
        value = m.priorite
        expected = 3
        self.assertTrue(value == expected)

    def testCloner(self):
        a = Paire(1, 2)
        b = a.cloner()
        self.assertTrue(a.eqPaire(b))

if __name__ == '__main__':
    unittest.main()

#####################################################

# Classe de test de la classe Arbre


import unittest
from Arbre import *
from copy import *


class TestArbre(unittest.TestCase):

    def setUp(self):
        self.node0 = Noeud(0)
        self.node1 = Noeud(1)
        self.node2 = Noeud(2)
        self.av1 = Arbre(None, None, None)
        self.av2 = Arbre(None, None, None)
        self.av3 = Arbre(None, None, None)
        self.a3 = Arbre(self.av1, self.node1, self.av2)
        self.a4 = Arbre(deepcopy(self.av1), self.node2, deepcopy(self.av2))

    def testEstVide1(self):
        self.assertTrue(self.av1.estVide())

    def testEstNonVide(self):
        self.a2 = (None, self.node0, None)
        self.assertFalse(self.a3.estVide())

    def testEstFeuille(self):
        self.assertTrue(self.a3.estFeuille())

    def testEstNonFeuille(self):
        a = Arbre(self.a3, self.node2, self.a4)
        self.assertFalse(a.estFeuille())

    def testEstNonFeuille2(self):
        a = Arbre(self.a3, self.node2, self.a4)
        self.assertFalse(a.estFeuille())

    def testArbreDroit(self):
        a = Arbre(self.a3, self.node2, self.a4)
        ad = a.getFd()
        self.assertTrue(ad is self.a4)

    def testSArbreGauche(self):
        a = Arbre(self.a3, self.node2, self.a4)
        ad = a.getFg()
        self.assertTrue(ad is self.a3)

if __name__ == '__main__':
    unittest.main()

################################################################


# Classe de test de la classe FilePrio


import unittest
from FilePrio import *

class TestFilePrio(unittest.TestCase):

    def testQueue(self):
        a = FilePrio([Paire(2, 4), Paire(3, 2),  Paire(6, 1)])
        a.queueFilePrio()
        value1 = a.fileprio[0].getElement()
        value2 = a.fileprio[0].getPriorite()
        value3 = a.fileprio[1].getElement()
        value4 = a.fileprio[1].getPriorite()
        expected1 = 3
        expected2 = 2
        expected3 = 6
        expected4 = 1
        self.assertTrue(value1 == expected1 and (value2 == expected2) and value3 == expected3 and value4 == expected4)

    def testTete(self):
        a = FilePrio([Paire(2, 4), Paire(3, 2), Paire(2, 3)])
        value1 = a.teteFilePrio().getElement()
        expected1 = 2
        value2 = a.teteFilePrio().getPriorite()
        expected2 = 4
        self.assertTrue(value1 == expected1 and value2 == expected2)

    def testEstVide(self):
        a = FilePrio([])
        self.assertTrue(a.estVide())

    def testEstNonVide(self):
        a = FilePrio([Paire(2, 4), Paire(3, 2), Paire(2, 3)])
        self.assertFalse(a.estVide())

    def testAjoutVide(self):
        a = FilePrio([])
        b = Paire(1, 2)
        a.ajout(b)
        expected1 = 1
        expected2 = 2
        value1 = a.fileprio[0].getElement()
        value2 = a.fileprio[0].getPriorite()
        self.assertTrue(value1 == expected1 and value2 == expected2)

    def testAjout1(self):
        a = FilePrio([Paire('B', 2), Paire('C', 3)])
        c = Paire('A', 1)
        a.ajout(c)
        value1 = a.fileprio[0].getElement()
        value2 = a.fileprio[0].getPriorite()
        expected1 = 'A'
        expected2 = 1
        self.assertTrue(value1 == expected1 and value2 == expected2 and value2 <= a.fileprio[1].getPriorite())

    def testAjoutMax(self):
        a = FilePrio([Paire('A', 2), Paire('B', 3)])
        c = Paire('C', 4)
        a.ajout(c)
        value1 = a.fileprio[-1].getElement()
        value2 = a.fileprio[-1].getPriorite()
        expected1 = 'C'
        expected2 = 4
        self.assertTrue(value1 is expected1 and value2 is expected2)

    def testAjoutQcq(self):
        a = FilePrio([Paire('A', 2), Paire('B', 3)])
        c = Paire('C', 3)
        a.ajout(c)
        value1 = a.fileprio[1].getElement()
        value2 = a.fileprio[1].getPriorite()
        expected1 = 'C'
        expected2 = 3
        self.assertTrue(value1 is expected1 and value2 is expected2)


if __name__ == '__main__':
    unittest.main()


#################################################
#                Module compresse               #
#################################################


# Module compresse contenant plusieurs fonctions détaillées dans le pdf

from FilePrio import *
from Paire import *
from Noeud import *


def lireFichier(nomFichier):
    """lit un fichier compris dans le même dossier"""
    fo = open(nomFichier, 'r')
    texte = fo.read()
    fo.close()
    return texte


def creerTabFreq(texte, nbcar):
    """retourne le nombre d'occurences de la lettre chr dans texte"""
    # à utiliser avec nbcar = 256
    assert texte != ""
    listefreq = [0] * nbcar
    for chr in texte:
        listefreq[ord(chr)] += 1
    return listefreq


def creerFilePriorite(tabfreq, nbcar):
    """retourne la file de priorité des lettres du textes selon leur nb d'occurrences"""
    fileprio = FilePrio([])
    for i in range(nbcar):
        if tabfreq[i] != 0:
            char = chr(i)
            A = Arbre(Arbre(None, None, None), Noeud(char), Arbre(None, None, None))
            fileprio.ajout(Paire(A, tabfreq[i]))
    return fileprio


def creerArbreCodage(fileprio):
    """crée l'arbre correspondant à la file de priorité"""
    while not fileprio.estVide():
        Paire1 = fileprio.teteFilePrio()
        fileprio.queueFilePrio()
        if fileprio.estVide():
            return Paire1.getElement()
        Paire2 = fileprio.teteFilePrio()
        fileprio.queueFilePrio()
        new = Paire(Arbre(Paire1.getElement(), Noeud(-1), Paire2.getElement()),
                    Paire1.getPriorite() + Paire2.getPriorite())
        fileprio.ajout(new)


def creerTabCode(arbrehufman, code, tabCode):
    """créer une table de codes (lettre, code)"""
    if arbrehufman.estFeuille():
        return [Paire(arbrehufman.getValRac(), code)]
    else:
        return tabCode + creerTabCode(arbrehufman.getFg(), code + "0", tabCode) + creerTabCode(arbrehufman.getFd(),
                                                                                               code + "1", tabCode)


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
        else:
            return "Erreur de codage"
        if start2.getValRac() != -1:
            decode += start2.getValRac()
            start = arbrehufman
        else:
            start = start2
    return decode


def tauxcompression(texte):
    """renvoie le taux de compression en %"""
    taux = 100 * len(
        coderTexte(texte, creerTabCode(creerArbreCodage(creerFilePriorite(creerTabFreq(texte, 256), 256)), "", []))) / (
           8 * (len(texte) - 1))
    return taux



##################################################
#       Classe de test du module compresse       #
##################################################

import unittest
from Compresse import *


class TestCompresse(unittest.TestCase):
    """classe de tests pour tester le module Compresse.py"""

    def setUp(self):
        self.texte1 = "Chabadabada"
        self.tabFreq1 = creerTabFreq(self.texte1, 256)
        self.file1 = creerFilePriorite(self.tabFreq1, 256)
        self.arbre1 = creerArbreCodage(self.file1)
        self.tabCode1 = creerTabCode(self.arbre1, "", [])
        self.texteCode1 = coderTexte(self.texte1, self.tabCode1)
        self.texteDecode1 = decoderTexte(self.texteCode1, self.arbre1)

        self.texte2 = "Tout language fini est régulier."
        self.tabFreq2 = creerTabFreq(self.texte2, 256)
        self.file2 = creerFilePriorite(self.tabFreq2, 256)
        self.arbre2 = creerArbreCodage(self.file2)
        self.tabCode2 = creerTabCode(self.arbre2, "", [])
        self.texteCode2 = coderTexte(self.texte2, self.tabCode2)
        self.texteDecode2 = decoderTexte(self.texteCode2, self.arbre2)

        texte = ""
        for i in range(256):
            texte += chr(i)
        self.texte3 = texte
        self.tabFreq3 = creerTabFreq(self.texte3, 256)
        self.file3 = creerFilePriorite(self.tabFreq3, 256)
        self.arbre3 = creerArbreCodage(self.file3)
        self.tabCode3 = creerTabCode(self.arbre3, "", [])
        self.texteCode3 = coderTexte(self.texte3, self.tabCode3)
        self.texteDecode3 = decoderTexte(self.texteCode3, self.arbre3)

        self.texte4 = "ab"
        self.tabFreq4 = creerTabFreq(self.texte4, 256)
        self.file4 = creerFilePriorite(self.tabFreq4, 256)
        self.arbre4 = creerArbreCodage(self.file4)
        self.tabCode4 = creerTabCode(self.arbre4, "", [])
        self.texteCode4 = coderTexte(self.texte4, self.tabCode4)
        self.texteDecode4 = decoderTexte(self.texteCode4, self.arbre4)

        self.texte5 = ""
        # pour tester creerArbreCodage
        self.vide = Arbre(None, None, None)
        self.node1 = Arbre(self.vide, Noeud('a'), self.vide)
        self.node2 = Arbre(self.vide, Noeud('b'), self.vide)
        self.node3 = Arbre(self.vide, Noeud('C'), self.vide)
        self.node4 = Arbre(self.vide, Noeud('d'), self.vide)
        self.node5 = Arbre(self.vide, Noeud('h'), self.vide)
        self.arbre = Arbre(self.node1, Noeud(-1), self.node2)
        self.node6 = Arbre(self.node5, Noeud(-1), self.node3)
        self.node7 = Arbre(self.node6, Noeud(-1), self.node4)
        self.node8 = Arbre(self.node2, Noeud(-1), self.node7)
        self.tree1 = Arbre(self.node1, Noeud(-1), self.node8)
        self.tree4 = Arbre(self.node2, Noeud(-1), self.node1)

    def testLireFichier(self):
        expected = self.texte1
        value = lireFichier("data.txt")
        self.assertTrue(value == expected)

    def testErreurCreerTab(self):
        self.assertRaises(AssertionError, creerTabFreq, self.texte5, 256)

    def testCreerTabFreq1(self):
        value = self.tabFreq1
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2,
                    0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertTrue(value == expected)

    def testCreerTabFreq2(self):
        value = creerTabFreq(self.texte3, 256)
        expected = [1] * 256
        self.assertEqual(value, expected)

    def testCreerArbre1(self):
        value = self.arbre1.ParcoursInfixe()
        expected = self.tree1.ParcoursInfixe()
        self.assertTrue(value == expected)

    def testCreerArbre2(self):
        value = self.arbre4.ParcoursInfixe()
        expected = self.tree4.ParcoursInfixe()
        self.assertTrue(value == expected)

    def testCreerTabCode1(self):
        expected = [('b', '0'), ('a', '1')]
        value = []
        tabCode = self.tabCode4
        for i in range(len(tabCode)):
            value += [(tabCode[i].getElement(), tabCode[i].getPriorite())]
        self.assertTrue(value == expected)

    def testCreerTabCode2(self):
        expected = [('a', '0'), ('b', '10'), ('h', '1100'), ('C', '1101'), ('d', '111')]
        value = []
        tabCode = self.tabCode1
        for i in range(len(tabCode)):
            value += [(tabCode[i].getElement(), tabCode[i].getPriorite())]
        self.assertTrue(value == expected)

    def testFilePrio(self):
        a = Paire(Arbre(Arbre(None, None, None), Noeud('h'), Arbre(None, None, None)), 1)
        b = Paire(Arbre(Arbre(None, None, None), Noeud('C'), Arbre(None, None, None)), 1)
        c = Paire(Arbre(Arbre(None, None, None), Noeud('d'), Arbre(None, None, None)), 2)
        d = Paire(Arbre(Arbre(None, None, None), Noeud('b'), Arbre(None, None, None)), 2)
        e = Paire(Arbre(Arbre(None, None, None), Noeud('a'), Arbre(None, None, None)), 5)
        H = [a, b, c, d, e]
        test = True
        for i in range(len(H)):
            if not (creerFilePriorite(self.tabFreq1, 256).fileprio[i].getPriorite() == H[i].getPriorite() and
                        (creerFilePriorite(self.tabFreq1, 256).fileprio[i].getElement().getValRac() ==
                             H[i].getElement().getValRac())):
                test = False
        self.assertTrue(test)

    def testFilePrio2(self):
        a = Paire(Arbre(Arbre(None, None, None), Noeud('b'), Arbre(None, None, None)), 1)
        b = Paire(Arbre(Arbre(None, None, None), Noeud('a'), Arbre(None, None, None)), 1)
        P = [a, b]
        test = True
        for i in range(len(P)):
            if not (creerFilePriorite(self.tabFreq4, 256).fileprio[i].getPriorite() == P[i].getPriorite() and
                        (creerFilePriorite(self.tabFreq4, 256).fileprio[i].getElement().getValRac() ==
                             P[i].getElement().getValRac())):
                test = False
        self.assertTrue(test)

    def testCoderTexte(self):
        value = self.texteCode1
        expected = "11011100010011101001110"
        self.assertTrue(value == expected)

    def testCoderTexte2(self):
        value = self.texteCode2
        expected = "011000111000001011101000100110111110000100111101111110011110011011001110111101001010111" \
                   "0101001000111000010000011111101001101"
        self.assertTrue(value == expected)

    def testCoderTexte3(self):
        value = self.texteCode3
        expected = "010101010101010001010111010101100101000101010000010100110101001001011101010111000101111101011" \
                   "110010110010101100001011011010110100100010101000100010001110100011001000001010000000100001101" \
                   "000010010011010100110001001111010011100100100101001000010010110100101001110101011101000111011" \
                   "101110110011100010111000001110011011100100111110101111100011111110111111001111001011110000111" \
                   "101101111010011001010110010001100111011001100110000101100000011000110110001001101101011011000" \
                   "110111101101110011010010110100001101011011010100001010100010100000101110001011000010001000100" \
                   "000001001100010010000111010001110000011111000111100001100100011000000110110001101000000101000" \
                   "001000000011100000110000000010000000000000011000000100000110100001100000011110000111000001001" \
                   "000010000000101100001010001101010011010000110111001101100011000100110000001100110011001000111" \
                   "101001111000011111100111110001110010011100000111011001110100010010100100100001001110010011000" \
                   "100001001000000010001100100010001011010010110000101111001011100010100100101000001010110010101" \
                   "011010101110101001101011111010110110100011101000011010011110100101101110111011100110111111101" \
                   "111011011001110110001101101111011010110001011100010011000111110001101100000111000000110000111" \
                   "100001011001101110011001100111111001110110010011100100011001011110010101111010111110100111101" \
                   "111111011011110001111100001111001111110010111111011111110011111111111111101111100111111000111" \
                   "110111111101011100101111001001110011111100110111000011110000011100011111000101110110111101100" \
                   "111011111110111011101001111010001110101111101010100101011001010010010111100101101001000110010" \
                   "000100100111001001010011101100111001001111110011110100110011001100010011011100110101000010110" \
                   "000100100001111000011010000001100000001000001110000010100011011000110010001111100011101000100" \
                   "110001000100010111000101010110101101101001011011110110110101100011011000010110011101100101011" \
                   "110110111100101111111011111010111001101110001011101110111010101001011010010010100111101001101" \
                   "01000011010000010100011101000101010110110101100101011111010111010101001101010001010101110101010"
        self.assertTrue(value == expected)

    def testCoderTexte4(self):
        value = self.texteCode4
        expected = "10"
        self.assertTrue(value == expected)

    def testDecoder1(self):
        value = self.texteDecode1
        expected = self.texte1
        self.assertTrue(value == expected)

    def testDecoder2(self):
        value = self.texteDecode2
        expected = self.texte2
        self.assertTrue(value == expected)

    def testDecoder3(self):
        value = self.texteDecode3
        expected = self.texte3
        self.assertTrue(value == expected)

    def testDecoder4(self):
        value = self.texteDecode4
        expected = "ab"
        self.assertTrue(value == expected)


if __name__ == '__main__':
    unittest.main()
