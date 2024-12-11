import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Valeurs a  prendre en compte
logging.info("Initialisation des constantes physiques et des paramètres généraux")
RHO = 1000 # masse volumique
ETA = 0.001 # coefficient de viscosité
DF = 15.5e-2 # diametre circulation froid
DC = 12e-3 # diametre circulation chaud
LAMDA = 0.6
CP = 4180
LF = 1
LC = 4
SC = np.pi*(DC / 2)**2
SF = np.pi*(DF / 2)**2
S = np.pi*2*(DC / 2)*LC

NB_MESURES = 8

# Fonctions de calcul
logging.info("Définition des fonctions utilitaires")

def reynolds(rho, eta, diameter, debitm):
    try:
        surface = np.pi*(diameter / 2)**2
        volume = debitm / (rho*surface)
        result = (rho*volume*diameter) / eta
        logging.debug(f"Reynolds calculé: {result}")
        return result
    except Exception as e:
        logging.error(f"Erreur lors du calcul de Reynolds: {e}")
        raise

def debit(m_eau, temps):
    try:
        res = m_eau / temps
        result = res*10**-3 # kg/s
        logging.debug(f"Débit calculé: {result}")
        return result
    except Exception as e:
        logging.error(f"Erreur lors du calcul du débit: {e}")
        raise

def incertitudes(k):
    try:
        moyenne = np.mean(k)
        ecart_type = np.std(k)
        result = (moyenne, ecart_type / np.sqrt(len(k)))
        logging.debug(f"Incertitudes calculées: {result}")
        return result
    except Exception as e:
        logging.error(f"Erreur lors du calcul des incertitudes: {e}")
        raise

def dtml_controle(tfe, tfs, tce, tcs):
    try:
        dtml_co =  ((tce-tfe)-(tcs-tfs)) / np.log((tce-tfe) / (tcs-tfs)) # Co_courant
        dtml_contre =  ((tce-tfs)-(tcs-tfe)) / np.log((tce-tfs) / (tcs-tfe))
        result = (dtml_co, dtml_contre, (dtml_co+dtml_contre) / 2)
        logging.debug(f"DTML contrôle calculé: {result}")
        return result
    except Exception as e:
        logging.error(f"Erreur lors du calcul de DTML contrôle: {e}")
        raise

def dtml(tfe, tfs, tce, tcs):
    try:
        dtml_co =  ((tce-tfe)-(tcs-tfs)) / np.log((tce-tfe) / (tcs-tfs)) # Co_courant
        dtml_contre =  ((tce-tfs)-(tcs-tfe)) / np.log((tce-tfs) / (tcs-tfe))
        result = (dtml_co+dtml_contre) / 2
        logging.debug(f"DTML calculé: {result}")
        return result
    except Exception as e:
        logging.error(f"Erreur lors du calcul de DTML: {e}")
        raise

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
Liste_donnees  =  [Mesure_1_1, Mesure_1_2]  # Ajouter d'autres mesures ici
Liste_Dmc = [mesure['Dmc'] for mesure in Liste_donnees]
Liste_h = [500 + i*10 for i in range(len(Liste_Dmc))]  # Exemple fictif pour h

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
