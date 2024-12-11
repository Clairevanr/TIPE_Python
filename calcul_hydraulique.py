
import numpy as np
import matplotlib.pyplot as plt
import logging

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



def ecart_relatif(chaud, froid):
    return (100*abs(chaud-froid)/froid)

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
