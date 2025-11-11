from calc import suma, resta, multiplicar, dividir


def test_suma():
    assert suma(2, 3) == 5


def test_resta():
    assert resta(5, 3) == 2


def test_multiplicar():
    assert multiplicar(4, 3) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_cero():
    import pytest
    with pytest.raises(ValueError, match="División por cero no permitida"):
        dividir(5, 0)
