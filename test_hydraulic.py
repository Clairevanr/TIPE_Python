import pytest
from calcul_hydraulique import reynolds, debit

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
