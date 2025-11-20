import pytest
from back.logic import calculate

def test_soma():
    assert calculate(2, "+", 3) == 5

def test_subtracao():
    assert calculate(5, "-", 2) == 3

def test_multiplicacao():
    assert calculate(4, "*", 5) == 20

def test_divisao_exata():
    # resultado inteiro, sem casas decimais
    assert calculate(10, "/", 2) == 5

def test_divisao_arredondada():
    # 2/3 = 0.666666... → 0.66667
    assert calculate(2, "/", 3) == 0.66667

def test_potencia():
    assert calculate(2, "^", 3) == 8

def test_potencia_arredondada():
    # 2^0.5 ≈ 1.41421
    assert calculate(2, "^", 0.5) == 1.41421

def test_raiz_quadrada_exata():
    assert calculate(9, "sqrt") == 3

def test_raiz_quadrada_arredondada():
    # sqrt(2) ≈ 1.41421
    assert calculate(2, "sqrt") == 1.41421

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(10, "/", 0)

def test_operacao_invalida():
    with pytest.raises(ValueError):
        calculate(1, "??", 2)
