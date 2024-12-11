import numpy as np
import matplotlib.pyplot as plt

from constantes_physiques import *
from calcul_hydraulique import *
from donnes import *

'''
This module allows me to treat theroritical calculation in order to confront it to my experimental results
'''

## Définitions des fonctions théoriques spécifiques 

def Redh(rho,eta,d,v):
    return rho*v*d / eta

def Prandtl(eta,cp,lamda):
    return eta*cp / lamda

#Correlation de Sieder et Tate: ecoulement laminaire
def Sieder(Pr,Re,D,L):
    return 1.86*(Pr*Re)**(1/3)*(D/L)**(1/3)



#CorrÃ©lation de Dittus-Boelter: ecoulement turbulent
def Dittus(Re,Pr):
    return 0.023*Re**0.8*Pr**(1/3)



#CorrÃ©lation de Hilpert: Ã©coulement autour du tube (C de©pend de Re)
def Hilpert(Re,Pr):
    if Re>=0.4 and  Re<=4.0:
        m=0.33
        C=0.989
    elif Re>=4.0 and Re<=40.0:
        m=0.466
        C=0.911
    elif Re>=40.0 and Re<=4000.0:
        m=0.466
        C=0.683
    elif Re>=4000.0 and Re<=40000.0:
        m=0.618
        C=0.193
    elif Re>=40000 and Re<=400000:
        m=0.805
        C=0.027
    
    return C*Re**m*Pr**(1/3)
 
    
def hi_coeff(D,LAMDA,v,RHO,ETA,CP,L):
    Re=Redh(RHO,ETA,D,v)
    Pr=Prandtl(ETA,CP,LAMDA)
    
    #if Re*Pr*D/L >=10:
     #   Nu=Sieder(Pr,Re,D,L)
      #  print('Sieder')
    if Re>=5000 and Pr>=0.6 and Pr<=100:
        Nu=Dittus(Re,Pr)
        print('Dittus')
    elif Pr>=0.5:
        Nu=Hilpert(Re,Pr)
        print('Hilpert')

    return Nu*LAMDA/D 
        
        

## Définition des listes utiles au tracé


Liste_Ref=[mesure['Ref'] for mesure in Liste_donnees]

Liste_Rec=[mesure['Rec'] for mesure in Liste_donnees]

Liste_Dmc=[mesure['Dmc'] for mesure in Liste_donnees]

Liste_rapport_debit=[mesure['Dmf']/mesure['Dmc'] for mesure in Liste_donnees]

Liste_vitesse_froid=[mesure['Dmf']/(RHO*SF) for mesure in Liste_donnees]

Liste_vitesse_chaud=[mesure['Dmc']/(RHO*SC) for mesure in Liste_donnees]




## CALCUL DU NOMBRE DU h ##

Liste_hf=[ hi_coeff(DF, LAMDA, Liste_vitesse_froid[i],RHO, ETA, CP, L) for i in range(len(Liste_donnees))]

Liste_hc=[ hi_coeff(DC, LAMDA, Liste_vitesse_chaud[i],RHO, ETA, CP, L) for i in range(len(Liste_donnees))]


plt.plot(Liste_Dmc,'o')
plt.xlabel('Dmc')
plt.ylabel('coeff échange convectif')
plt.title('Théorie')
plt.show()







