import pytest
from tipe_theorie import Prandtl

'''
This test module allow to test the theoritical function. I designed the test for the Prandtl number to illustrate
'''

def test_Prandtl():
    # Test de Prandtl
    eta = 0.001
    cp = 4180
    lamda = 0.6
    expected = 6.9667
    assert Prandtl(eta, cp, lamda) == pytest.approx(expected, rel=1e-3)

