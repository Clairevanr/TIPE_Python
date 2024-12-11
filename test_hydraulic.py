import pytest
from calcul_hydraulique import reynolds, debit, incertitudes, dtml

'''
This test module allow to test physical formulas related functions. I designed the test for some functions
from the calcul_hydraulique module
'''


def test_reynolds():
    # Données d'entrée
    rho = 1000
    eta = 0.001
    diameter = 0.012
    debitm = 0.2  # kg/s

    # Résultat attendu (calculé manuellement)
    surface = 3.14159 * (diameter / 2) ** 2
    volume = debitm / (rho * surface)
    expected = (rho * volume * diameter) / eta

    # Appel de la fonction
    result = reynolds(rho, eta, diameter, debitm)

    # Assertion
    assert pytest.approx(result, rel=1e-5) == expected

def test_debit():
    # Données d'entrée
    m_eau = 1467  # grammes
    temps = 9.44  # secondes

    # Résultat attendu (en kg/s)
    expected = 1467 / 9.44 * 1e-3

    # Appel de la fonction
    result = debit(m_eau, temps)

    # Assertion
    assert pytest.approx(result, rel=1e-5) == expected


def test_incertitudes():
    k = [1, 2, 3, 4, 5]  # Exemple de données

    # Résultat attendu
    moyenne = sum(k) / len(k)
    ecart_type = (sum((x - moyenne) ** 2 for x in k) / len(k)) ** 0.5
    expected_moyenne = moyenne
    expected_erreur = ecart_type / (len(k) ** 0.5)

    # Appel de la fonction et vérification
    result_moyenne, result_erreur = incertitudes(k)
    assert pytest.approx(result_moyenne, rel=1e-5) == expected_moyenne
    assert pytest.approx(result_erreur, rel=1e-5) == expected_erreur
