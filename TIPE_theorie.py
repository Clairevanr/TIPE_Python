import numpy as np
import matplotlib.pyplot as plt

rho=1000  #masse volumique 
eta=0.001  #coefficient de viscositÃ©
Df=15.5e-2  #diametre circulation froid
Dc=12e-3  #diamètre circulation chaud
lamda=0.6
cp=4180
L=1
Sc=np.pi*(Dc/2)**2
Sf=np.pi*(Df/2)**2
e=2e-3


# FONCTIONS

def Reynolds(rho,eta,D,Dm):
    S=np.pi*(D/2)**2
    v=Dm/(rho*S)
    return (rho*v*D)/eta

def debit(meau,temps):  
    debit=meau/temps
    return debit*10**-3 #kg/s

def Nusselt(h,D,lamda):
    return (h*D)/lamda

def Prandtl(eta,cp,lamda):
    return (eta*cp)/lamda

def Redh(rho,eta,D,Dm):
    S=np.pi*(D/2)**2
    v=Dm/(rho*S)
    Dh=(4*(D/2)**2 * np.pi)/(2*np.pi*D/2)
    return (rho*v*Dh)/eta

#STOCKAGE DES DONNEES:
    
#Salve 1:    
Mesure_1_1={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':32.8 , 'Tcs': 43.7, 'Tfe': 28.2, 'Tce': 56.5}  #Initialisation d'un dictionnaire de donnees
Mesure_1_2={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs': 34, 'Tcs': 48.5, 'Tfe': 28.2, 'Tce': 53.0}
    
Mesure_1_3={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs': 30.9, 'Tcs': 34.9, 'Tfe': 28.9, 'Tce': 37.7}
Mesure_1_4={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':30.5, 'Tcs': 36.2, 'Tfe': 28.9, 'Tce': 39.1}

Mesure_1_5={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':30.5, 'Tcs': 38.7, 'Tfe': 28, 'Tce':  47.5}
Mesure_1_6={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':31.3, 'Tcs': 44.1, 'Tfe': 28, 'Tce': 52}
Mesure_1_7={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':30.9, 'Tcs': 41.4, 'Tfe': 27.9, 'Tce': 48}
Mesure_1_8={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':32.1, 'Tcs': 42.5, 'Tfe': 28.9, 'Tce': 57.2}
Mesure_1_9={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':31.3, 'Tcs': 37.7, 'Tfe': 28.9, 'Tce': 52.4}
Mesure_1_10={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':34.2, 'Tcs': 49.5, 'Tfe': 29.3, 'Tce': 54.4}

Mesure_1_11={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':29.9, 'Tcs': 32.2, 'Tfe': 27.5, 'Tce': 48.6}
Mesure_1_12={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':29.4, 'Tcs': 32.4, 'Tfe': 28.2, 'Tce': 48.2} 
Mesure_1_13={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':34, 'Tcs': 47.9, 'Tfe': 29.3, 'Tce': 55}
Mesure_1_14={'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':32.8, 'Tcs': 41.9, 'Tfe': 29.2, 'Tce': 54.3}  

#MESURES DE DEBIT
#SALVE 1  
Mesure_1_1['Dmf']=debit(1467,9.44)
Mesure_1_1['Dmc']=debit(273,5)

Mesure_1_2['Dmf']=debit(1471,11.4)
Mesure_1_2['Dmc']=debit(1198,7.45)

Mesure_1_3['Dmf']=debit(1442,10.68)
Mesure_1_3['Dmc']=debit(832,8.26)

Mesure_1_4['Dmf']=debit(1442,10.68)
Mesure_1_4['Dmc']=(debit(636,8.37)+debit(598,8))/2

Mesure_1_5['Dmf']=debit(2564,19.21)
Mesure_1_5['Dmc']=(debit(464,11.61)+debit(448,11.55))/2

Mesure_1_6['Dmf']=debit(2564,19.21)
Mesure_1_6['Dmc']=debit(1594,10.58)

Mesure_1_7['Dmf']=debit(1699,12.90)
Mesure_1_7['Dmc']=(debit(1067,11.55) + debit(1144,0.093))/2

Mesure_1_8['Dmf']=debit(1245,8.40)
Mesure_1_8['Dmc']=(debit(277,6.33)+debit(299,7.72))/2

Mesure_1_9['Dmf']=debit(1262,9.48)
Mesure_1_9['Dmc']=(debit(202,8.53)+debit(213,10.30))/2

Mesure_1_10['Dmf']=debit(1461, 11.07)
Mesure_1_10['Dmc']=(debit(1268,9.36)+debit(1477,10.61))/2

Mesure_1_11['Dmf']=debit(1537, 10.24)
Mesure_1_11['Dmc']=(debit(149,6.18)+debit(145,6.77))/2

Mesure_1_12['Dmf']=debit(974, 7.05)
Mesure_1_12['Dmc']=(debit(153,14.46)+debit(116,10.77))/2

Mesure_1_13['Dmf']=debit(1061,7.90)
Mesure_1_13['Dmc']=(debit(274,3.15)+debit(275,3.16))/2

Mesure_1_14['Dmf']=debit(1087,8.27)
Mesure_1_14['Dmc']=debit(224,5.63)


#CALCUL DE REYNOLDS

#SALVE 1
Mesure_1_1['Ref']=Reynolds(rho, eta, Df, Mesure_1_1['Dmf'])
Mesure_1_1['Rec']=Reynolds(rho, eta, Dc, Mesure_1_1['Dmc'])

Mesure_1_2['Ref']=Reynolds(rho, eta, Df, Mesure_1_2['Dmf'])
Mesure_1_2['Rec']=Reynolds(rho, eta, Dc, Mesure_1_2['Dmc'])

Mesure_1_3['Ref']=Reynolds(rho, eta, Df, Mesure_1_3['Dmf'])
Mesure_1_3['Rec']=Reynolds(rho, eta, Dc, Mesure_1_3['Dmc'])

Mesure_1_4['Ref']=Reynolds(rho, eta, Df, Mesure_1_4['Dmf'])
Mesure_1_4['Rec']=Reynolds(rho, eta, Dc, Mesure_1_4['Dmc'])

Mesure_1_5['Ref']=Reynolds(rho, eta, Df, Mesure_1_5['Dmf'])
Mesure_1_5['Rec']=Reynolds(rho, eta, Dc, Mesure_1_5['Dmc'])

Mesure_1_6['Ref']=Reynolds(rho, eta, Df, Mesure_1_6['Dmf'])
Mesure_1_6['Rec']=Reynolds(rho, eta, Dc, Mesure_1_6['Dmc'])

Mesure_1_7['Ref']=Reynolds(rho, eta, Df, Mesure_1_7['Dmf'])
Mesure_1_7['Rec']=Reynolds(rho, eta, Dc, Mesure_1_7['Dmc'])

Mesure_1_8['Ref']=Reynolds(rho, eta, Df, Mesure_1_8['Dmf'])
Mesure_1_8['Rec']=Reynolds(rho, eta, Dc, Mesure_1_8['Dmc'])

Mesure_1_9['Ref']=Reynolds(rho, eta, Df, Mesure_1_9['Dmf'])
Mesure_1_9['Rec']=Reynolds(rho, eta, Dc, Mesure_1_9['Dmc'])

Mesure_1_10['Ref']=Reynolds(rho, eta, Df, Mesure_1_10['Dmf'])
Mesure_1_10['Rec']=Reynolds(rho, eta, Dc, Mesure_1_10['Dmc'])

Mesure_1_11['Ref']=Reynolds(rho, eta, Df, Mesure_1_11['Dmf'])
Mesure_1_11['Rec']=Reynolds(rho, eta, Dc, Mesure_1_11['Dmc'])

Mesure_1_12['Ref']=Reynolds(rho, eta, Df, Mesure_1_12['Dmf'])
Mesure_1_12['Rec']=Reynolds(rho, eta, Dc, Mesure_1_12['Dmc'])

Mesure_1_13['Ref']=Reynolds(rho, eta, Df, Mesure_1_13['Dmf'])
Mesure_1_13['Rec']=Reynolds(rho, eta, Dc, Mesure_1_13['Dmc'])

Mesure_1_14['Ref']=Reynolds(rho, eta, Df, Mesure_1_14['Dmf'])
Mesure_1_14['Rec']=Reynolds(rho, eta, Dc, Mesure_1_14['Dmc'])


Liste_donnees = [Mesure_1_1,Mesure_1_2, Mesure_1_3, Mesure_1_4, Mesure_1_10, Mesure_1_12, Mesure_1_13, Mesure_1_14]


Liste_Ref=[mesure['Ref'] for mesure in Liste_donnees]

Liste_Rec=[mesure['Rec'] for mesure in Liste_donnees]

Liste_Dmc=[mesure['Dmc'] for mesure in Liste_donnees]

Liste_rapport_debit=[mesure['Dmf']/mesure['Dmc'] for mesure in Liste_donnees]

Liste_vitesse_froid=[mesure['Dmf']/(rho*Sf) for mesure in Liste_donnees]

Liste_vitesse_chaud=[mesure['Dmc']/(rho*Sc) for mesure in Liste_donnees]

Liste_Redh=[Redh(rho, eta, Dc, Liste_Dmc[i]) for i in range(len(Liste_donnees))]

#CorrÃ©lation de Sieder et Tate: Ã©coulement laminaire
def Sieder(Pr,Re,D,L):
    return 1.86*(Pr*Re)**(1/3)*(D/L)**(1/3)



#CorrÃ©lation de Dittus-Boelter: Ã©coulement turbulent
def Dittus(Re,Pr):
    return 0.023*Re**0.8*Pr**(1/3)



#CorrÃ©lation de Hilpert: Ã©coulement autour du tube (C dÃ©pend de Re)
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
 
    
def hi_coeff(D,lamda,v,rho,eta,cp,L):
    Re=Redh(rho,eta,D,v)
    Pr=Prandtl(eta,cp,lamda)
    
    #if Re*Pr*D/L >=10:
     #   Nu=Sieder(Pr,Re,D,L)
      #  print('Sieder')
    if Re>=5000 and Pr>=0.6 and Pr<=100:
        Nu=Dittus(Re,Pr)
        print('Dittus')
    elif Pr>=0.5:
        Nu=Hilpert(Re,Pr)
        print('Hilpert')

    return Nu*lamda/D 
        
#On néglige l'encrassement
        
def h_coeff(hf,hc,e, lamda):
     return 1/((1/hc) + (e/lamda)  + (1/hf))


## CALCUL DU NOMBRE DU h ##

Liste_hf=[ hi_coeff(Df, lamda, Liste_vitesse_froid[i],rho, eta, cp, L) for i in range(len(Liste_donnees))]

Liste_hc=[ hi_coeff(Dc, lamda, Liste_vitesse_chaud[i],rho, eta, cp, L) for i in range(len(Liste_donnees))]


Liste_h=[ h_coeff(Liste_hf[i], Liste_hc[i], e,lamda) for i in range(len(Liste_donnees)) ]

plt.plot(Liste_Dmc, Liste_h, 'o')
plt.xlabel('Dmc')
plt.ylabel('coeff échange convectif')
plt.title('Théorie')
plt.show()







