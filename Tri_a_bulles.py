myTable=[87,75,15,26,84,74]
minimum=100
donnee=0
numList=0

for i in range (0,len(myTable)):

    for n in range (i,len(myTable)):
        
        if(myTable[n]<minimum):
            minimum=myTable[n]
            numList=n

    donnee=myTable[i]
    myTable[i]=minimum
    myTable[numList]=donnee
    minimum=100

print(myTable)

# Le tri à bulles est très lent car il doit vérifier à chaque fois la liste entière moins la derniere 
# valeur modifier pour vérifier que l'ordre établie est respecter.
# 
# Il va chercher la plus petite valeur et la comparer à toutes les autres pour vérifier qu'elle est 
# bien la plus petite, le temps de son éxecution dépendra du nombre de valeur dans la liste myTable.