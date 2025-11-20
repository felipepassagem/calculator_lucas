import math

def round_output(value):
    value = round(float(value), 5)          # limita para 5 decimais
    # remove zeros desnecessários e ponto final
    return float(f"{value:.5f}".rstrip("0").rstrip("."))


def calculate(a, op, b=None):
    a = float(a)

    if op == "+":
        return round_output(a + float(b))
    if op == "-":
        return round_output(a - float(b))
    if op == "*":
        return round_output(a * float(b))
    if op == "/":
        return round_output(a / float(b))
    if op == "^":
        return round_output(a ** float(b))
    if op == "sqrt":
        return round_output(math.sqrt(a))

    raise ValueError("Operação inválida")
