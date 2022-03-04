import numpy as np
import matplotlib.pyplot as plt
import fileinput
from scipy import optimize


kb=1.380649e-23
#Conversion des , en . pour pouvoir récupérer les données



#Récupération des données

def fit(p0,func,Liste1,Liste2):
    params, cv = optimize.curve_fit(func,Liste1,Liste2,p0)
    return params

A=[]
B=[]
C=[[]]
D=[[]]
for i in range(1,10):
    #Conversion des , en . pour éviter les erreurs avec la fonction np.loadtxt
    f = open(f"Data{i}.txt",'r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace(",",".")
    f = open(f"Data{i}.txt",'w')
    f.write(newdata)
    f.close()
    #Récupération des données du fichier sous forme de tableau
    l=np.loadtxt(f"Data{i}.txt")
    #Récupération de tout les paramètres selon les 2 méthodes grace a la fonction fit
    A.append(fit(1.7,(lambda T,alpha:np.power(T,alpha)),l[:,0],l[:,1]))
    B.append(np.average(np.divide(np.log(l[:,1]),np.log(l[:,0]))))
    C.append([fit((0.1,3800),lambda T,R,Delta:R*np.exp(Delta/T),l[:,0],l[:,2])[0],fit((0.1,3800),lambda T,R,Delta:R*np.exp(Delta/T),l[:,0],l[:,2])[1]*kb*6.242e18])
    D.append([fit((0.1,3800),lambda T,R,Delta:(np.log(R)+Delta*T),1/l[:,0],np.log(l[:,2]))[0],fit((0.1,3800),lambda T,R,Delta:(np.log(R)+Delta*T),1/l[:,0],np.log(l[:,2]))[1]*kb*6.242e18])

#Impression des données dans un fichier
F= open('Resultats.txt','w')
for j in range(len(A)):
    F.write("Fit S1 | Fit logarithme S1 | Fit S2 [R_0,Delta] | Fit Logarithmes S2 [R_0,Delta]")
    F.write(str(A[j])+str(B[j])+str(C[j])+str(D[j])+"\n")
    
F.close()






