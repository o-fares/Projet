# classe de tests FilePrio
import unittest
from copy import *
from Paire import *

from FilePrio import *

class TestFilePrio(unittest.TestCase):

    def testQueue(self):
        a = FilePrio([Paire(2,4),Paire(3,2),Paire(6,1)])
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
        a = FilePrio([Paire(2,4),Paire(3,2),Paire(2,3)])
        value1 = a.teteFilePrio().getElement()
        expected1 = 2
        value2 = a.teteFilePrio().getPriorite()
        expected2 = 4
        self.assertTrue(value1 == expected1 and value2 == expected2)

    def testEstVide(self):
        a = FilePrio([])
        self.assertTrue(a.estVide())

    def testEstNonVide(self):
        a = FilePrio([Paire(2,4),Paire(3,2),Paire(2,3)])
        self.assertFalse(a.estVide())

    def testAjoutVide(self):
        a = FilePrio([])
        b = Paire(1,2)
        a.ajout(b)
        expected1 = 1
        expected2 = 2
        value1 = a.fileprio[0].getElement()
        value2 = a.fileprio[0].getPriorite()
        self.assertTrue(value1 == expected1 and value2 == expected2)

    def testAjout1(self):
        a = FilePrio([Paire('B',2),Paire('C',3)])
        c = Paire('A',1)
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
