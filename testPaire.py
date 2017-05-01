
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
