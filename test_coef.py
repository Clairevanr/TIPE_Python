import pytest
from tipe_theorie import Prandtl



def test_Prandtl():
    # Test de Prandtl
    eta = 0.001
    cp = 4180
    lamda = 0.6
    expected = 6.9667
    assert Prandtl(eta, cp, lamda) == pytest.approx(expected, rel=1e-3)

