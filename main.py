# coding:UTF-8

from fonctions import *

print("\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("\t\t\t$$               PROGRAMME DE CALCUL DU PGCD/PPCM DES POLYNOMES                $$")
print("\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


A = []
B = []
ppcm  =[]
value1 = []
value2 = []

n = '0'
while type(n) != int or n <= 0:
    n = input("\n\n\tVeuillez entrer le nombre de monomes du polynome 1: ")
    try:
        n = int(n)
    except:
        print("\tERREUR:Vous devez entrer un entier")          
for i in range(n):
	saisir_polynome(A,i+1)

n = '0'	
while type(n) != int or n <= 0:
    n = input("\n\n\tVeuillez entrer le nombre de monomes du polynome 2: ")
    try:
        n = int(n)
    except:
        print("\tERREUR:Vous devez entrer un entier")        

for j in range(n):
	saisir_polynome(B,j+1)


if(A[0][0] == 0 and B[0][0] != 0):
	ppcm = [[0,0]]
elif((A[0][0] == 0 or A[0][0] != 0) and B[0][0] == 0):
	print("\n\t\tOPERATION IMPOSSIBLE\n")
	exit(0)
elif(A[0][0] != 0  and B[0][0] != 0):
	ppcm = PPCM(A,B) 					# On choisis d'afficher le PGCD a l'interieur de la fonction qui nous renvoie le PPCM

print("PPCM :",ppcm)






