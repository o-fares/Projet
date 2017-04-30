import unittest
from Compresse import *

class TestCompresse(unittest.TestCase) :
    """classe de tests pour tester le module Compresse.py"""

    def setUp(self) :
        self.texte1 = "Chabadabada"
        self.tabFreq1 = creerTabFreq(self.texte1, 256)
        self.file1 = creerFilePriorite(self.tabFreq1, 256)
        self.arbre1 = creerArbreCodage(self.file1)
        self.tabCode1 = creerTabCode(self.arbre1,"", [])
        self.texteCode1 = coderTexte(self.texte1, self.tabCode1)
        self.texteDecode1 = decoderTexte(self.texteCode1, self.arbre1)

        self.texte2 = "Tout language fini est régulier."
        self.tabFreq2 = creerTabFreq(self.texte2,256)
        self.file2 = creerFilePriorite(self.tabFreq2,256)
        self.arbre2 = creerArbreCodage(self.file2)
        self.tabCode2 = creerTabCode(self.arbre2,"",[])
        self.texteCode2 = coderTexte(self.texte2,self.tabCode2)
        self.texteDecode2 = decoderTexte(self.texteCode2,self.arbre2)

        texte = ""
        for i in range(256):
            texte += chr(i)
        self.texte3 = texte
        self.tabFreq3 = creerTabFreq(self.texte3,256)
        self.file3 = creerFilePriorite(self.tabFreq3,256)
        self.arbre3 = creerArbreCodage(self.file3)
        self.tabCode3 = creerTabCode(self.arbre3, "", [])
        self.texteCode3 = coderTexte(self.texte3, self.tabCode3)
        self.texteDecode3 = decoderTexte(self.texteCode3, self.arbre3)

        self.texte4 = "ab"
        self.tabFreq4 = creerTabFreq(self.texte4,256)
        self.file4 = creerFilePriorite(self.tabFreq4,256)
        self.arbre4 = creerArbreCodage(self.file4)
        self.tabCode4 = creerTabCode(self.arbre4, "", [])
        self.texteCode4 = coderTexte(self.texte4, self.tabCode4)
        self.texteDecode4 = decoderTexte(self.texteCode4, self.arbre4)

    def testDecoder1(self):
        value = self.texteDecode1
        expected = "Chabadabada"
        self.assertTrue(value == expected)

    def testDecoder2(self):
        value = self.texteDecode2
        expected = "Tout language fini est régulier."
        self.assertTrue(value == expected)

    def testDecoder3(self):
        value = self.texteDecode3
        expected = self.texte3
        self.assertTrue(value == expected)

    def testDecoder4(self):
        value = self.texteDecode4
        expected = "ab"
        self.assertTrue(value == expected)

    def testCoderTexte(self):
        value = self.texteCode1
        expected = "11011100010011101001110"
        self.assertTrue(value == expected)

    def testCoderTexte2(self):
        value = self.texteCode2
        expected = "0110001110000010111010001001101111100001001111011111100111100110110011101111010010101110101001000111000010000011111101001101"
        self.assertTrue(value == expected)

    def testCoderTexte3(self):
        value = self.texteCode3
        expected = "01010101010101000101011101010110010100010101000001010011010100100101110101011100010111110101111001011001010110000101101101011010010001010100010001000111010001100100000101000000010000110100001001001101010011000100111101001110010010010100100001001011010010100111010101110100011101110111011001110001011100000111001101110010011111010111110001111111011111100111100101111000011110110111101001100101011001000110011101100110011000010110000001100011011000100110110101101100011011110110111001101001011010000110101101101010000101010001010000010111000101100001000100010000000100110001001000011101000111000001111100011110000110010001100000011011000110100000010100000100000001110000011000000001000000000000001100000010000011010000110000001111000011100000100100001000000010110000101000110101001101000011011100110110001100010011000000110011001100100011110100111100001111110011111000111001001110000011101100111010001001010010010000100111001001100010000100100000001000110010001000101101001011000010111100101110001010010010100000101011001010101101010111010100110101111101011011010001110100001101001111010010110111011101110011011111110111101101100111011000110110111101101011000101110001001100011111000110110000011100000011000011110000101100110111001100110011111100111011001001110010001100101111001010111101011111010011110111111101101111000111110000111100111111001011111101111111001111111111111110111110011111100011111011111110101110010111100100111001111110011011100001111000001110001111100010111011011110110011101111111011101110100111101000111010111110101010010101100101001001011110010110100100011001000010010011100100101001110110011100100111111001111010011001100110001001101110011010100001011000010010000111100001101000000110000000100000111000001010001101100011001000111110001110100010011000100010001011100010101011010110110100101101111011011010110001101100001011001110110010101111011011110010111111101111101011100110111000101110111011101010100101101001001010011110100110101000011010000010100011101000101010110110101100101011111010111010101001101010001010101110101010"
        self.assertTrue(value == expected)

    def testCoderTexte4(self):
        value = self.texteCode4
        expected = "10"
        self.assertTrue(value == expected)

    def testFilePrio(self):
        a = Paire(Arbre(Arbre(None,None,None),Noeud('h'),Arbre(None,None,None)),1)
        b = Paire(Arbre(Arbre(None,None,None),Noeud('C'),Arbre(None,None,None)),1)
        c = Paire(Arbre(Arbre(None,None,None),Noeud('d'),Arbre(None,None,None)),2)
        d = Paire(Arbre(Arbre(None,None,None),Noeud('b'),Arbre(None,None,None)),2)
        e = Paire(Arbre(Arbre(None,None,None),Noeud('a'),Arbre(None,None,None)),5)
        H = [a,b,c,d,e]
        value = self.file1
        test = True
        for i in range(len(H)):
            if not(creerFilePriorite(self.tabFreq1, 256).fileprio[i].getPriorite() == H[i].getPriorite() and
                       (creerFilePriorite(self.tabFreq1, 256).fileprio[i].getElement().getValRac() == H[i].getElement().getValRac())):
                test = False
        self.assertTrue(test)

    def testFilePrio2(self):
        a = Paire(Arbre(Arbre(None,None,None),Noeud('b'),Arbre(None,None,None)),1)
        b = Paire(Arbre(Arbre(None,None,None),Noeud('a'),Arbre(None,None,None)),1)
        P = [a,b]
        test = True
        for i in range(len(P)):
            if not(creerFilePriorite(self.tabFreq4, 256).fileprio[i].getPriorite() == P[i].getPriorite() and
                       (creerFilePriorite(self.tabFreq4, 256).fileprio[i].getElement().getValRac() == P[i].getElement().getValRac())):
                test = False
        self.assertTrue(test)






if __name__ == '__main__':
    unittest.main()


