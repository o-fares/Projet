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
        self.node3 = Arbre(self.vide, Noeud('c'), self.vide)
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

