import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from calcul_hydraulique import *
from constantes_physiques import *
from donnes import *

'''
This module is made to test an equation I obtained thanks to an approximation. It allows me to verify its consistency
'''


## Définition listes utiles au tracé des graphes


Liste_Ref = [mesure['Ref'] for mesure in Liste_donnees]
Liste_Rec = [mesure['Rec'] for mesure in Liste_donnees]
Liste_Dmc = [mesure['Dmc'] for mesure in Liste_donnees]
Liste_Dmf = [mesure['Dmf'] for mesure in Liste_donnees]
Liste_Tfs = [mesure['Tfs'] for mesure in Liste_donnees]
Liste_Tcs = [mesure['Tcs'] for mesure in Liste_donnees]
Liste_Tfe = [mesure['Tfe'] for mesure in Liste_donnees]
Liste_Tce = [mesure['Tce'] for mesure in Liste_donnees]
Liste_vitesses=[ mesure['Dmc']/(RHO*SC) for mesure in Liste_donnees ]



##CALCULS ROBUSTESSE DE (1):
    
Chaud_1= [mesure['Dmc']*(mesure['Tce'] - mesure['Tcs']) for mesure in Liste_donnees]

Froid_1= [mesure['Dmf']*(mesure['Tfs'] - mesure['Tfe']) for mesure in Liste_donnees]


ecart= [ecart_relatif(Chaud_1[i], Froid_1[i]) for i in range(len(Chaud_1))]

plt.plot(range(1,len(ecart)+1), ecart,'x')
plt.xlabel('Mesures')
plt.ylabel('écart relatif (%)')
plt.title('Validité de (1)')
plt.show()
