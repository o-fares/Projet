# NOM: OUADAHI
# PRENOM: Fares
# DATE DE CREATION: 11/02/2017
# NOM DU FICHIER: OUADAHI-exoFibo.py

import time

t0=time.clock() # temps de début
c=0 # création d'une variable qui sert de compteur à la fonction récursive
def fibo(n):
    global c
    c=c+1
    if n<2:
        return 1
    return fibo(n-1)+fibo(n-2)


def fibo1(n):
    cpt=1 # compteur à 1 pour n= 0 ou 1
    f1=1
    f2=1
    for i in range(2,n+1):
        cpt,f1,f2=cpt+1,f2,f1+f2
    return f2,cpt

# tests du temps entre le début et la fin de la fonction + nombre d'additions

n=6
print(fibo(n),time.clock()-t0,c)

# compteur du nombre d'additions effectuées par la seconde fonction

print(fibo1(n))
