
import unittest

from Noeud import *
from Arbre import *
from copy import *

class TestArbre(unittest.TestCase):

    def setUp(self) :
        self.node0 = Noeud(0)
        self.node1 = Noeud(1)
        self.node2 = Noeud(2)
        self.av1 = Arbre(None,None,None)
        self.av2 = Arbre(None,None,None)
        self.av3 = Arbre(None,None,None)
        self.a3 = Arbre(self.av1, self.node1, self.av2)
        self.a4 = Arbre(deepcopy(self.av1), self.node2, deepcopy(self.av2))

    def testEstVide1(self):
        self.assertTrue(self.av1.estVide())

    def testEstNonVide(self):
        self.a2 = (None, self.node0,None)
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
        self.assertTrue( ad is self.a3)


if __name__ == '__main__':
    unittest.main()
