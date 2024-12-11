import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import logging

## Imports des fonctions de calcul et des constantes physiques

from calcul_hydraulique import *
from constantes_physiques import *
from donnes import *



# Configuration des logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Fonctions de calcul
logging.info("Définition des fonctions utilitaires")

# Stockage des données
logging.info("Stockage des données initiales")
Mesure_1_1 = {'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs':32.8 , 'Tcs': 43.7, 'Tfe': 28.2, 'Tce': 56.5}
Mesure_1_2 = {'Ref': 0, 'Rec': 0 ,'Dmf':0, 'Dmc':0, 'Tfs': 34, 'Tcs': 48.5, 'Tfe': 28.2, 'Tce': 53.0}
# Ajouter d'autres mesures ici...

# Calcul des débits
logging.info("Calcul des débits pour chaque mesure")
Mesure_1_1['Dmf'] = debit(1467,9.44)
Mesure_1_1['Dmc'] = debit(273,5)
Mesure_1_2['Dmf'] = debit(1471,11.4)
Mesure_1_2['Dmc'] = debit(1198,7.45)

# Calcul des nombres de Reynolds
logging.info("Calcul des nombres de Reynolds pour chaque mesure")
Mesure_1_1['Ref'] = reynolds(RHO, ETA, DF, Mesure_1_1['Dmf'])
Mesure_1_1['Rec'] = reynolds(RHO, ETA, DC, Mesure_1_1['Dmc'])
Mesure_1_2['Ref'] = reynolds(RHO, ETA, DF, Mesure_1_2['Dmf'])
Mesure_1_2['Rec'] = reynolds(RHO, ETA, DC, Mesure_1_2['Dmc'])

# Liste des données sélectionnées pour les graphiques

Liste_Dmc = [mesure['Dmc'] for mesure in Liste_donnees]
Liste_h = [500 + i*10 for i in range(len(Liste_Dmc))]  # Exemple fictif pour h
Liste_Rec = [mesure['Rec'] for mesure in Liste_donnees]

# Graphiques
logging.info("Génération des graphiques")

# Première courbe
plt.plot(Liste_Dmc, Liste_h, 'o')
plt.title('h en fonction de Dmc')
plt.xlabel('Dmc')
plt.ylabel('h')
logging.info("Affichage du premier graphique: h en fonction de Dmc")
plt.show()

# Deuxième courbe
for (Dmc, Rec) in zip(Liste_Dmc, [mesure['Rec'] for mesure in Liste_donnees]):
    plt.plot(Dmc, Rec, color='red' if Rec >= 2000 else 'green', marker="o")
plt.xlabel('Dmc')
plt.ylabel('Nombre de Reynolds')
plt.title('Nature de l\'écoulement côté chaud en fonction du débit')
plt.grid()
logging.info("Affichage du deuxième graphique: Nature de lécoulement")
plt.show()

# TROISIEME COURBE


for (Dmc, h , Rec) in zip(Liste_Dmc, Liste_h, Liste_Rec):
    plt.plot(Dmc,h, color  =  test_nature_color(Rec), marker  = "o", label = test_nature(Rec))
plt.xlabel('Dmc')
plt.ylabel('h')
plt.title('h selon la nature de l\'écoulement')

laminaire_patch = mpatches.Patch(color = "green", label  =  "Laminaire")
turbulent_patch = mpatches.Patch(color = "red", label  =  "Turbulent")

plt.legend(handles  =  [laminaire_patch, turbulent_patch])
plt.grid()
plt.show()
