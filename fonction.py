# coding:UTF-8


def saisir_polynome(polynome,i):
    print("\n  Monome",i,"\n")
    
    a = '0'
    while type(a) != float:
        a = input("Coefficient : ")
        try:
           a = float(a)
        except:
            print("\tERREUR:Vous devez entrer un reel pour le coefficient")        
    
    b = '0'
    while type(b) != int :
        b = input("Degre : ")
        try:
           b = int(b)
        except:
            print("\tERREUR:Vous devez entrer un entier pour le degre")        

    monome = [a, b]  # Entree des valeurs de notre polynome
    insert(polynome,monome)
    print(polynome)

# ----------------------------------------------------------------------------- #

def insert(polynome,monome): # Fonction qui inserre un monome dans un polynome a sa position exacte
    position = 0.5
    if len(polynome) == 0:
        polynome.append(monome)
        position = 1.5
    else:
        for i in range(0, len(polynome)):
            if polynome[i][1] == monome[1]:
                position = i
    if position == 0.5:
        polynome.append(monome)
    elif position != 0.5 and position != 1.5:
        polynome[position][0] += monome[0]  # Entrer les monomes du polynome et l'addition des monomes a coefficients identiques
    ranger(polynome)  # Ranger les monomes par ordre de puissances afin de faciliter la division avec notre fonction range()
    
# -----------------------------------------------------------------------#

def ranger(polynome):
    monome = [] 
    posi_null = []  # liste qui contiendra les indices des monomes de coefficients nulls
    if len(polynome) == 0:
        return monome
    else:
        for i in range(len(polynome)):
            for j in range(len(polynome) - 1):
                if polynome[j][1] < polynome[j + 1][1]:
                    polynome.insert(j, polynome[j + 1])
                    del polynome[j + 2]  # Fonction pour classer les monomes de nos polynomes par ordre de degre

   
    for j in range(len(polynome)):
        if polynome[j][0] == 0:  # Ici je veux supprimer tous les monomes de coefficient 0,alors je stock les indices ou les
            	           	 # coefficients sont nulls dans posi_null
            posi_null.append(j)

    for i in range(len(posi_null)):
        if len(polynome) != 1: # ici on se rend compte que si la taille est egale a 1 et que l'on fait un del, la liste sera 
                        # innexistante on ne pourra plus acceder a la liste alors on teste si  sa taille est superieur ou nom a 1            
            del polynome[posi_null[i] - i]
        elif len(polynome) == 1 and polynome[0][0] == 0: #Ici on considere la cas ou la taille de liste est 1 et on lui affecte alors tout simplement une liste vide 
            monome2 = []                          # et dinc de taille zero
            polynome = monome2                   

# ----------------------------------------------------------------------- #

def soustraction(polynome1, polynome2):
    monome = []

    for j in range(len(polynome2)):
        monome = (polynome2[j])
        monome[0] = monome[0]*(-1)
        insert(polynome1,monome)

    ranger(polynome1)
    return polynome1

# ------------------------------------------------------------ #


def produitPolynomial(polynome1, polynome2):
    produitPolynomes = []
    monome = []

    if len(polynome1) == 0 or len(polynome2) == 0:
        return monome
    for k in range(len(polynome1)):
        for j in range(len(polynome2)):
            a = (polynome1[k][0] * polynome2[j][0])
            b = (polynome1[k][1] + polynome2[j][1])
            monome = [a, b]
            insert(produitPolynomes,monome)
            
    ranger(produitPolynomes)
    return produitPolynomes

# ----------------------------------------------------------------------- #

'''
Notre fonction de division doit retourner un reste et le diviseur avec poly1 = devidende et poly2 = diviseur
alors il effectue la dividsion tant que le degre du dividende est superieur a celle du diviseur 
ASTUCE: Tant que le monome de plus haut degre du dividende est superieur a celle du diviseur alors on effectue la division 
        et dans ce cas le diviseur recupere a chaque fois le dividende recupere le reste 
'''
def divisionEuclidienne(polynome1,polynome2):
    quotient = []
    reste = []
    monome = []
    monome2 = []
    prod = []

    if(polynome2[0][1] == 0): #Ici on teste le cas ou le diviseur serais un monome de degre 0 et si c'est le cas on effectue juste 
                          # une division par son coefficient  
        for i in range(len(polynome1)):
            polynome1[i][0] = polynome1[i][0]/polynome2[0][0]
        return polynome2,monome,polynome1

    while polynome1[0][1] >= polynome2[0][1]:     

        a = polynome1[0][0]/polynome2[0][0]
        b = polynome1[0][1]-polynome2[0][1]
        monome = [a,b]        #  Ici,je recupere la valeur de la division du monome du plus haut degre du dividende par celui du diviseur
        quotient.append(monome)  #    J'affecte la valeur du resultat a la liste nommee: 'qoutient'  
        monome2.append(quotient[-1]) #    Ici je recupere le dernier monome qui a ete affecte au resultat et je fais son produitPolynomial par le dividende
        print("Quotient",quotient,"\n")                         #      NB: On aurait juste pu faire le produitPolynomial par la derniere valeur du quotient      
        prod = produitPolynomial(polynome2,monome2)
        reste = soustraction(polynome1,prod) #   Reste de la soustraction du dividende par le produitPolynomial de la derniere valeur du quotient
        polynome1 = reste
        if polynome1[0][0] == 0:        #Ici je dis que si le reste de la division est nulle alors j'arrete l'operation
            return polynome2,polynome1,quotient
        print("Rest:",reste,"\n")
        del monome2[0]

    return polynome2,polynome1,quotient  #Ici polynome1 est notre R et polynome2 notre B  

# ----------------------------------------------------------------------- #

def PGCD(polynome1,polynome2):    
    quotient = []
    pgcd = []

    if polynome1[0][1] < polynome2[0][1]: # Cas ou l'indice de du polynome 1 est inferieur a celui du polynome 2:Alors on effectue tout simplement une permutation
        permut = []
        permut = polynome1
        polynome1 = polynome2
        polynome2 = permut

    if(polynome1[0][1] == polynome2[0][1] and len(polynome1) < len(polynome2)): # Cas ou les polynomes sont de meme degre mais ou le nombre de monomes est different
        permut = []
        permut = polynome1
        polynome1 = polynome2
        polynome2 = permut

    while polynome2[0][1] != 0:
        if(polynome2[0][0] == 0):   # Cas ou le reste de la division est zero
            pgcd = polynome1
            pgcd[0][0] = pgcd[0][0]/pgcd[0][0]
            return pgcd
        
        pgcd = polynome2
        polynome1,polynome2,quotient = divisionEuclidienne(polynome1,polynome2)

    if(polynome2[0][0] != 0): 
        pgcd = polynome2   
            
    if pgcd[0][0] != 1:     #Cette partie me permet d'unitariser mon polynome au cas ou le coefficient est differrent de zero
        simplifier = pgcd[0][0]   #Ici je recupere le coefficient du monome de plus haut degre si celui-ci est differrente de 1
        for i in range(len(pgcd)):
            pgcd[i][0] = (pgcd[i][0]/simplifier)

    if pgcd[0][1] == 0:
        a = []
        a = [[1,0]]
        pgcd = a

    return pgcd

# ------------------------------------------------------------ #

def PPCM(polynome1,polynome2):
    prod = []
    pgcd = []
    ppcm = []
    A = []
    B = []
    dividentDivision = []
    resteDivision = []

    A = polynome1
    B = polynome2
    prod = produitPolynomial(polynome1,polynome2)
    pgcd = PGCD(A,B)
    print("Produit",prod)
    dividentDivision,resteDivision,ppcm = divisionEuclidienne(prod,pgcd)

    print("\n\nPGCD:",pgcd,"\n")

    return ppcm
