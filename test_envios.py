import pytest
from envios import calc

# Resultados esperados calculados a mano con la especificación (R1 a R8),
# no con lo que devuelve el código heredado.
# (id, peso, zona, cliente, dia, cupon, esperado)
CASOS = [
    ("CP-01", 3, "nacional", "vip", 6, "ENVIO10", 8200),
    ("CP-02", 12, "rural", "normal", 3, None, 11700),
    ("CP-03", 3, "urbana", "normal", 6, None, 8000),
    ("CP-04", 2, "urbana", "vip", 2, None, 5100),
    ("CP-05", 3, "urbana", "frecuente", 2, "ENVIO10", 5100),
    ("CP-06", 5, "urbana", "frecuente", 2, None, 8600),
    ("CP-08", 0.01, "urbana", "normal", 2, None, 6000),
    ("CP-09", 3.01, "urbana", "normal", 2, None, 9000),
    ("CP-10", 10, "urbana", "normal", 2, None, 9000),
    ("CP-11", 10.01, "urbana", "normal", 2, None, 9000),
    ("CP-12", 50, "urbana", "normal", 2, None, 41000),
    ("CP-15", 5, "nacional", "normal", 2, None, 13100),
    ("CP-16", 5, "urbana", "normal", 7, None, 11000),
    ("CP-17", 5, "urbana", "vip", 2, "ENVIO10", 6900),
    ("CP-18", 5, "urbana", "frecuente", 2, "ENVIO10", 7700),
    ("CP-19", 3, "urbana", "normal", 2, None, 6000),
    ("CP-20", 5, "rural", "vip", 5, None, 8400),
    ("CP-21", 2, "urbana", "vip", 2, "ENVIO10", 5000),
]


@pytest.mark.parametrize("id_, p, z, c, d, cup, esperado", CASOS)
def test_costo(id_, p, z, c, d, cup, esperado):
    assert calc(p, z, c, d, cup) == esperado


def test_cp07_peso_cero():
    with pytest.raises(ValueError):
        calc(0, "urbana", "normal", 2)


def test_peso_sobre_maximo():
    with pytest.raises(ValueError):
        calc(50.01, "urbana", "normal", 2)


def test_cp13_zona_invalida():
    with pytest.raises(ValueError):
        calc(5, "aerea", "normal", 2)


def test_cp14_dia_invalido():
    with pytest.raises(ValueError):
        calc(5, "urbana", "normal", 8)


def test_cupon_inexistente_es_error():
    with pytest.raises(ValueError):
        calc(3, "urbana", "normal", 2, "PROMO5")


# Solicitud de cambio: hora pico (17 a 19 inclusive, +8 % despues de la zona)
# (id, peso, zona, cliente, dia, cupon, hora, esperado)
CASOS_HORA = [
    ("HP-01", 5, "urbana", "normal", 2, None, 17, 9700),
    ("HP-02", 5, "urbana", "normal", 2, None, 19, 9700),
    ("HP-03", 5, "urbana", "normal", 2, None, 16, 9000),
    ("HP-04", 5, "urbana", "normal", 2, None, 20, 9000),
    ("HP-05", 5, "rural", "vip", 6, None, 18, 10800),
    ("HP-06", 5, "urbana", "normal", 2, None, 0, 9000),
    ("HP-07", 5, "urbana", "normal", 2, None, 23, 9000),
]


@pytest.mark.parametrize("id_, p, z, c, d, cup, hora, esperado", CASOS_HORA)
def test_hora_pico(id_, p, z, c, d, cup, hora, esperado):
    assert calc(p, z, c, d, cup, hora) == esperado


def test_hp08_hora_mayor_a_23():
    with pytest.raises(ValueError):
        calc(5, "urbana", "normal", 2, None, 24)


def test_hp09_hora_negativa():
    with pytest.raises(ValueError):
        calc(5, "urbana", "normal", 2, None, -1)