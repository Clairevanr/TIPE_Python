
import numpy as np
import matplotlib.pyplot as plt
import logging

'''
This module provides basic functions for hydraulic calculus, such as Reynolds number or a flow rate
'''

def reynolds(rho, eta, diameter, debitm):
    '''
    Returns the Reynold number
    '''

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
    '''
    Returns the flow rate 
    '''
    try:
        res = m_eau / temps
        result = res*10**-3 # kg/s
        logging.debug(f"Débit calculé: {result}")
        return result
    except Exception as e:
        logging.error(f"Erreur lors du calcul du débit: {e}")
        raise

def dtml_controle(tfe, tfs, tce, tcs):
    '''
    Returns a logarithmic mean of temperature difference with a controle applicated
    '''
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
    '''
    Returns the logarithmic mean of temperature difference
    '''
    try:
        dtml_co =  ((tce-tfe)-(tcs-tfs)) / np.log((tce-tfe) / (tcs-tfs)) # Co_courant
        dtml_contre =  ((tce-tfs)-(tcs-tfe)) / np.log((tce-tfs) / (tcs-tfe))
        result = (dtml_co+dtml_contre) / 2
        logging.debug(f"DTML calculé: {result}")
        return result
    except Exception as e:
        logging.error(f"Erreur lors du calcul de DTML: {e}")
        raise
    
def test_nature(Rec):
    '''
    Returns whether the flow is turbulent or not
    '''
    if Rec>=2000:
        return('Turbulent') # Turbulent
    else:
        return('Laminaire') # Laminaire


'''
This part is dedicated to handling mesures incertainty
'''


def ecart_relatif(chaud, froid):
    '''
    Returns the relative difference between two loops
    '''
    return (100*abs(chaud-froid)/froid)

def incertitudes(k):
    '''
    Returns the mesure incertainties
    '''
    try:
        moyenne = np.mean(k)
        ecart_type = np.std(k)
        result = (moyenne, ecart_type / np.sqrt(len(k)))
        logging.debug(f"Incertitudes calculées: {result}")
        return result
    except Exception as e:
        logging.error(f"Erreur lors du calcul des incertitudes: {e}")
        raise
