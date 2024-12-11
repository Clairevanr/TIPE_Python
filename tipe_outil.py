import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



#Valeurs a  prendre en compte

rho=1000  #masse volumique 
eta=0.001  #coefficient de viscosite
Df=15.5e-2  #diametre circulation froid
Dc=12e-3  #diametre circulation chaud
lamda=0.6
cp=4180
Lf=1
Lc=4
Sc=np.pi*(Dc/2)**2
Sf=np.pi*(Df/2)**2
S=np.pi*2*(Dc/2)*Lc

Nb_mesures=8

#Fonctions de calcul:  Ecoulement

def Reynolds(rho,eta,D,Dm):
    S=np.pi*(D/2)**2
    v=Dm/(rho*S)
    return (rho*v*D)/eta

def debit(meau,temps):  
    debit=meau/temps
    return debit*10**-3 #kg/s
    
def cal_efficacite(Tce,Tcs,Tfe,Tfs,Dmc,Dmf):
    Pf=Dmf*4.18*(Tfs-Tfe)
    Pc=Dmc*4.18*(Tcs-Tce)
    
    if abs(Pf)>abs(Pc):
        e=(Tce-Tcs)/(Tce-Tfe)
    else:
        e=(Tfs-Tfe)/(Tce-Tfe)
    return e

    

def incertitudes(K):
    moyenne=np.mean(K)
    ecart_type=np.std(K)
    return(moyenne, ecart_type/np.sqrt((len(K))))

def DTML_controle(Tfe, Tfs, Tce, Tcs):
    Dtmlco= ((Tce-Tfe)-(Tcs-Tfs))/np.log((Tce-Tfe)/(Tcs-Tfs)) #Co_courant
    Dtmlcontre= ((Tce-Tfs)-(Tcs-Tfe))/np.log((Tce-Tfs)/(Tcs-Tfe))
    return (Dtmlco, Dtmlcontre, (Dtmlco+Dtmlcontre)/2)

def DTML(Tfe, Tfs, Tce, Tcs):
    Dtmlco= ((Tce-Tfe)-(Tcs-Tfs))/np.log((Tce-Tfe)/(Tcs-Tfs)) #Co_courant
    Dtmlcontre= ((Tce-Tfs)-(Tcs-Tfe))/np.log((Tce-Tfs)/(Tcs-Tfe))
    return  (Dtmlco+Dtmlcontre)/2

'''  #Calcul de vitesses
vf=Dmf/(rho*Sf) #vitesse du fluide froid
vc=Dmc/(rho*Sc) #vitesse du fluide chaud
'''

#STOCKAGE DES DONNEES:
    
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


#SAL


Liste_donnees = [Mesure_1_2, Mesure_1_3, Mesure_1_4, Mesure_1_10,Mesure_1_12,Mesure_1_13, Mesure_1_14]

Liste_Ref = [mesure['Ref'] for mesure in Liste_donnees]
Liste_Rec = [mesure['Rec'] for mesure in Liste_donnees]
Liste_Dmc = [mesure['Dmc'] for mesure in Liste_donnees]
Liste_Dmf = [mesure['Dmf'] for mesure in Liste_donnees]
Liste_Tfs = [mesure['Tfs'] for mesure in Liste_donnees]
Liste_Tcs = [mesure['Tcs'] for mesure in Liste_donnees]
Liste_Tfe = [mesure['Tfe'] for mesure in Liste_donnees]
Liste_Tce = [mesure['Tce'] for mesure in Liste_donnees]
Liste_vitesses=[ mesure['Dmc']/(rho*Sc) for mesure in Liste_donnees ]

Liste_rapport_debit=[mesure['Dmf']/mesure['Dmc'] for mesure in Liste_donnees]

Liste_efficacite=[cal_efficacite(mesure['Tce'],mesure['Tcs'],mesure['Tfe'], mesure['Tfs'], mesure['Dmc'], mesure['Dmf']) for mesure in Liste_donnees]

Liste_DTML_controle=[DTML_controle(mesure['Tfe'], mesure['Tfs'],mesure['Tce'],mesure['Tcs']) for mesure in Liste_donnees]
Liste_DTML=[DTML(mesure['Tfe'], mesure['Tfs'],mesure['Tce'],mesure['Tcs']) for mesure in Liste_donnees]

Chaud_1= [mesure['Dmc']*(mesure['Tce'] - mesure['Tcs']) for mesure in Liste_donnees]

Froid_1= [mesure['Dmf']*(mesure['Tfs'] - mesure['Tfe']) for mesure in Liste_donnees]

Puissance=[np.mean([Chaud_1[i]*cp,Froid_1[i]*cp]) for i in range(len(Chaud_1))]

Liste_h= [Puissance[i]/(S*Liste_DTML[i]) for i in range(len(Liste_DTML))]

#Test nature écoulement:  
def test_nature_color(Rec):
    if Rec>=2000:
        return('red') # Turbulent
    else:
        return('green') # Laminaire
    
def test_nature(Rec):
    if Rec>=2000:
        return('Turbulent') # Turbulent
    else:
        return('Laminaire') # Laminaire
    
    
#Calcul de K global (moyen):
    
def incertitudes(Liste_K):
    moyenne=np.mean(Liste_K)
    ecart_type=np.std(Liste_K)
    return(moyenne, ecart_type/np.sqrt((len(Liste_K))))




# PREMIERE COURBE
Liste_Rapport_Debit = []
for (Dmc, efficacite , Rec) in zip(Liste_Dmc, Liste_efficacite, Liste_Rec):
    plt.plot(Dmc,efficacite, color = test_nature_color(Rec), marker ="o", label=test_nature(Rec))
plt.xlabel('Dmc')
plt.ylabel('efficacité')
plt.title('Efficacité en fonction du rapport des débits')

laminaire_patch = mpatches.Patch(color="green", label = "Laminaire")
turbulent_patch = mpatches.Patch(color="red", label = "Turbulent")

plt.legend(handles = [laminaire_patch, turbulent_patch])
plt.grid()
plt.show()

# DEUXIEME COURBE:
    
plt.plot( Liste_Dmc,Liste_h,'o')
plt.title('h en fonction de Dmc')
plt.xlabel('Dmc')
plt.ylabel('h')
plt.show()

# TROISIEME COURBE
for (Dmc , Rec) in zip(Liste_Dmc, Liste_Rec):
    plt.plot(Dmc,Rec, color = test_nature_color(Rec), marker ="o", label=test_nature(Rec))
plt.xlabel('Dmc')
plt.ylabel('Nombre de Reynolds')
plt.title('Nature de l\'écoulement côté chaud en fonction du débit')

laminaire_patch = mpatches.Patch(color="green", label = "Laminaire")
turbulent_patch = mpatches.Patch(color="red", label = "Turbulent")
plt.legend(handles = [laminaire_patch, turbulent_patch])
plt.grid()
plt.show()

# QUATRIEME COURBE


for (Dmc, h , Rec) in zip(Liste_Dmc, Liste_h, Liste_Rec):
    plt.plot(Dmc,h, color = test_nature_color(Rec), marker ="o", label=test_nature(Rec))
plt.xlabel('Dmc')
plt.ylabel('h')
plt.title('h selon la nature de l\'écoulement')

laminaire_patch = mpatches.Patch(color="green", label = "Laminaire")
turbulent_patch = mpatches.Patch(color="red", label = "Turbulent")

plt.legend(handles = [laminaire_patch, turbulent_patch])
plt.grid()
plt.show()
