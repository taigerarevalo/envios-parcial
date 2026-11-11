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
]


@pytest.mark.parametrize("id_, p, z, c, d, cup, esperado", CASOS)
def test_costo(id_, p, z, c, d, cup, esperado):
    assert calc(p, z, c, d, cup) == esperado


def test_peso_sobre_maximo():
    with pytest.raises(ValueError):
        calc(50.01, "urbana", "normal", 2)


def test_cupon_inexistente_es_error():
    with pytest.raises(ValueError):
        calc(3, "urbana", "normal", 2, "PROMO5")