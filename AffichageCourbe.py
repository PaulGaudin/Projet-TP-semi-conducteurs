import numpy as np
import matplotlib.pyplot as plt
import fileinput
from scipy import optimize


kb=1.380649e-23
#Conversion des , en . pour pouvoir récupérer les données
f = open('Data1.txt','r')
filedata = f.read()
f.close()
newdata = filedata.replace(",",".")
f = open('Data1.txt','w')
f.write(newdata)
f.close()


#Récupération des données
l=np.loadtxt('Data1.txt')


plt.subplot(2,2,1)

#Création de la fonction de fit de la courbe de S1 par une fonction de type R=T**alpha
def fitS1():
    p0=(1.7)
    params, cv = optimize.curve_fit(lambda t,Alpha: np.power(t,Alpha),l[:,0],l[:,1],p0)
    return params

#Affichage de la courbe et de son fit
alpha=fitS1()
plt.plot(l[:,0],l[:,1],label='S1')
plt.plot(l[:,0],np.power(l[:,0],alpha),label='Fit S1')
plt.title(f"Alpha = {alpha}")
plt.xlabel('Température')
plt.ylabel('Résistance')
plt.legend()



plt.subplot(2,2,2)

#Création de la fonction de fit de la courbe de S2 par une fonction de type R=R_0*exp(Delta/(kb*T))
def fitS2():
    p0=(0.1,3800)
    params, cv = optimize.curve_fit(lambda t,R,Delta:R*np.exp(Delta/t),l[:,0],l[:,2],p0)
    return params



#Affichage de la courbe et de son fit
R,Delta=fitS2()
plt.plot(l[:,0],l[:,2],label='S2')
plt.plot(l[:,0],R*np.exp(Delta/l[:,0]),label='Fit')
plt.title(f"R_0 = {R} Ohms, Delta = {Delta*kb*6.242e18} eV")
plt.xlabel('Température')
plt.ylabel('Résistance')
plt.legend()



plt.subplot(2,2,3)


#On effectue un fit en récupérant la valeur moyenne de ln(R)/ln(T) sur toute la courbe, et en prenant cette valeur comme pente
Alpha=np.average(np.divide(np.log(l[:,1]),np.log(l[:,0])))


#Affichage de la courbe et de son fit
plt.plot(np.log(l[:,0]),np.log(l[:,1]),label='S1')
plt.plot(np.log(l[:,0]),np.log(l[:,0])*Alpha,label='Fit 2')
plt.title(f"Alpha = {Alpha}")
plt.xlabel('ln(Température)')
plt.ylabel('ln(Résistance)')
plt.legend()


plt.subplot(2,2,4)



#On effectue un fit d'une droite affine de ln(R) en fonction de 1/T, pour récupérer l'ordonnée a l'origine et la pente de cette droite

def fitS22():
    p0=(0.1,3800)
    params, cv = optimize.curve_fit(lambda t,R,Delta:(np.log(R)+Delta*t),1/l[:,0],np.log(l[:,2]),p0)
    return params

#Affichage de la courbe et de son fit
R,Delta=fitS22()
plt.plot(1/l[:,0],np.log(l[:,2]),label='S2')
plt.plot(1/l[:,0],np.log(R)+Delta/l[:,0],label='Fit')
plt.title(f"R_0 = {R} Ohms, Delta = {Delta*kb*6.242e18} eV")
plt.xlabel('ln(Température)')
plt.ylabel('ln(Résistance)')

plt.legend()
plt.show()