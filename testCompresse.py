import unittest
from Noeud import *
from Arbre import *
from Paire import *
from FilePrio import *
from Compresse import *

class TestCompresse(unittest.TestCase) :
    """classe de tests pour tester le module Compresse.py"""

    def setUp(self) :
        self.texte1 = lireFichier("data.txt")
        self.tabFreq1 = creerTabFreq(self.texte1, 53)
        self.file1 = creerFilePriorite(self.tabFreq1, 53)
        self.arbre1 = creerArbreCodage(self.file1)
        self.tabCode1 = creerTabCode(self.arbre1,"", [])
        self.texteCode1 = coderTexte(self.texte1, self.tabCode1)
        self.texteDecode1 = decoderTexte(self.texteCode1, self.arbre1)
