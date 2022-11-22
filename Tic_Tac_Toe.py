
J1 = "X"
J2 = "O"

exempleP1=[1,2,3]
exempleP2=[4,5,6]
exempleP3=[7,8,9]

conditionV=0

while (conditionV!=1):

    C1=""
    C2=""
    C3=""
    C4=""
    C5=""
    C6=""
    C7=""
    C8=""
    C9=""



    Separation = "|"

    tableauP1 = [C1,Separation,C2,Separation,C3]
    tableauP2 = [C4,Separation,C5,Separation,C6]
    tableauP3 = [C7,Separation,C8,Separation,C9]

    
    
    print("----------Numéro Cases----------")
    print(exempleP1)
    print(exempleP2)
    print(exempleP3)
    print("--------------------------------")


    print (tableauP1) 
    print (tableauP2) 
    print (tableauP3) 
    print("-------------------------------")
    print('Joueur 1 veuillez choisir le numéro de la case à jouer')

    ChoixNJ1=input("N°")
    ChoixJ1 = "C" + ChoixNJ1

    C1= C1 +"X"
    print(ChoixJ1)

    print (tableauP1)
    print (tableauP2)
    print (tableauP3)
    conditionV=1

    



