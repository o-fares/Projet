# Projet
Projet d'info

# Projet groupe informatique à rendre pour le 1er mai 23h55
Réaliser le codage de Huffmann
Travail fait:
- classes Paire, FilePrio, Arbre ✓
- classe de tests pour chacune des classes ✓
- module compresse qui donne les fonctions permettant de lire un texte/le compresser/le décompresser ✓ 
détail des fonctions:
    - lireFichier(nomFichier) ✓
    - creerTabFreq(texte, nbcar) ✓
    - creerFilePriorite(tabfreq, nbcar) ✓
    - creeArbreCodage(fileprio) ✓
    - creerTabCodes(arbrehufman, code, tabcodes) ✓
    - coderTexte(texte, tabcodes) ✓
    - decoderTexte(textecode, arbrehufman) ✓

- 5 avril: présentation des classes implémentant les structures de données et leurs classes de tests ✓

- 14 avril: présentation de l'avancement du projet. 10 min max par groupe ✓

# Travail à faire :
- classe de test du module compresse:
idées pour la classe de test:
- un setup avec tous les éléments utiles pour le test
test de chaque fonction :
    - lireFichier: s'assurer que le texte affiché 
    - creerTabFreq: s'assurer que la table affichée correspond aux attentes, à tester pour:
        - un texte vide
        - en majuscules
        - en minuscules
        - texte quelconque
    - creerFilePriorite: s'assurer que la file prio retournée est celle attendue, tester avec:
        - file prio vide
        - file prio quelconque
    - creeArbreCodage: s'assurer que la fonction retourne le bon arbre, tester pour:
        - arbre vide
        - 1 caractère (juste un fils gauche ou un fils droit)
        - 2 caractères (arbre binaire)
    - creerTabCodes(arbrehufman, code, tabcodes): ???
    - coderTexte(texte, tabcodes): s'assurer que le texte codé correspond aux éléments de la table
        - texte vide
        - 1 caractère
        - texte quelconque
    - decoderTexte(textecode, arbrehufman): s'assurer que l'on puisse décoder le texte
        - texte quelconque
        - un caractère
        - un caractère qui n'est pas dans l'arbre
- fichiers sources des classes et du module compresse + classes de tests
- fichier IDF-SOURCES.pdf contenant l'ensemble du code formaté par a2ps puis ps2pdf (IDF = nom en majuscules du chef du projet)
- fichier IDF-Rapport.pdf expliquant ce qui a été fait, les tests réalisés et les difficultés rencontrées

# à lire: 
 
- Apprendre à manipuler des fichiers avec Python: page 107 http://inforef.be/swi/download/apprendre_python3_5.pdf
- TD arbres: exercices 4 et 5 utiles pour le projet
- cours sur les arbres: compression de Hufman page 8 à 11 (Ametice)
