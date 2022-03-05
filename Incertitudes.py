import numpy as np

Delta=np.array([0.316,0.308,0.326,0.326,0.294,0.280,0.331,0.261,0.324,0.326,0.321,0.321,0.330,0.325,0.324,0.312])
Alpha=np.array([1.229,1.224,1.231,1.214,1.212,1.216,1.229,1.206,1.232,1.227,1.223,1.230,1.213,1.211,1.214,1.227,1.206,1.232])
vnames={Delta[0]:"Delta",Alpha[0]:"Alpha"}
for Echant in [Delta,Alpha]:

    Moy=0

    for i in range(Echant.size):
        Moy+=Echant[i]

    Moy*=1/(Echant.size)

    sigma=0

    for u in range(Echant.size):
        sigma+= (Echant[i]-Moy)**2

    sigma*=1/(Echant.size-1)
    sigma=np.sqrt(sigma)

    U=3.97*sigma/np.sqrt(Echant.size)

    print(vnames[Echant[0]], " :\n ","Taille d'échantillion : ",Echant.size,"\nMoyenne : ",Moy, "\nIncertitude : ", U)
