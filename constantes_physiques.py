
## Constantes physiques fixes
import numpy as np

RHO = 1000 #masse volumique
ETA = 0.001 #coefficient de viscosite
DF = 15.5e-2 #diametre circulation froid
DC = 12e-3 #diametre circulation chaud
LAMDA = 0.6 
CP = 4180 #Capacité thermique
LF = 1 #Longueur système froid
LC = 4 #Longueur système chaud
SC = np.pi*(DC / 2)**2 #Surface arrivée système chaud
SF = np.pi*(DF / 2)**2 #Surface arrivée système froid
S = np.pi*2*(DC / 2)*LC #Surface cylindre

