# envios.py · v2.0.0 (refactorizado)

CONFIG = {
    "L1": 3,
    "L2": 10,
    "RECARGO_RURAL": 0.10,
    "RECARGO_NACIONAL": 0.45,
    "DESC_VIP": 0.15,
    "RECARGO_FINDE": 2000,
}

# Constantes con nombre (antes eran numeros magicos)
PESO_MAXIMO = 50
DIA_MINIMO = 1
DIA_MAXIMO = 7
DIA_SABADO = 6
TARIFA_TRAMO_1 = 6000
TARIFA_TRAMO_2 = 9000
TARIFA_POR_KG_EXTRA = 800
COSTO_MINIMO = 5000
DESCUENTO_FRECUENTE = 0.05
DESCUENTO_ENVIO10 = 0.10
PASO_REDONDEO = 100
HORA_MINIMA = 0
HORA_MAXIMA = 23
HORA_PICO_INICIO = 17
HORA_PICO_FIN = 19
RECARGO_HORA_PICO = 0.08


# Patron Estrategia: una clase por zona, todas con el mismo metodo
class ZonaUrbana:
    def aplicar(self, tarifa):
        return tarifa


class ZonaRural:
    def aplicar(self, tarifa):
        return tarifa + tarifa * CONFIG["RECARGO_RURAL"]


class ZonaNacional:
    def aplicar(self, tarifa):
        return tarifa + tarifa * CONFIG["RECARGO_NACIONAL"]


ZONAS = {
    "urbana": ZonaUrbana(),
    "rural": ZonaRural(),
    "nacional": ZonaNacional(),
}


def validar_entradas(peso, zona, dia, hora=None):
    if peso <= 0 or peso > PESO_MAXIMO:
        raise ValueError("peso invalido")
    if zona not in ZONAS:
        raise ValueError("zona invalida")
    if dia < DIA_MINIMO or dia > DIA_MAXIMO:
        raise ValueError("dia invalido")
    if hora is not None and (hora < HORA_MINIMA or hora > HORA_MAXIMA):
        raise ValueError("hora invalida")


def tarifa_base(peso):
    if peso <= CONFIG["L1"]:
        return TARIFA_TRAMO_1
    if peso <= CONFIG["L2"]:
        return TARIFA_TRAMO_2
    return TARIFA_TRAMO_2 + (peso - CONFIG["L2"]) * TARIFA_POR_KG_EXTRA


def recargo_fin_de_semana(dia):
    if dia >= DIA_SABADO:
        return CONFIG["RECARGO_FINDE"]
    return 0
def recargo_hora_pico(valor, hora):
    if hora is not None and HORA_PICO_INICIO <= hora <= HORA_PICO_FIN:
        return valor + valor * RECARGO_HORA_PICO
    return valor


def descuento_cliente(valor, cliente):
    if cliente == "frecuente":
        return valor - valor * DESCUENTO_FRECUENTE
    if cliente == "vip":
        return valor - valor * CONFIG["DESC_VIP"]
    return valor


def aplicar_cupon(valor, cupon):
    if cupon is None:
        return valor
    if cupon == "ENVIO10":
        return valor - valor * DESCUENTO_ENVIO10
    raise ValueError("cupon invalido")


def redondear_a_cien(valor):
    mitad = PASO_REDONDEO / 2
    return int((round(valor, 2) + mitad) // PASO_REDONDEO) * PASO_REDONDEO


def calc(peso, zona, cliente, dia, cupon=None, hora=None):
    validar_entradas(peso, zona, dia, hora)
    total = tarifa_base(peso)
    total = ZONAS[zona].aplicar(total)
    total = recargo_hora_pico(total, hora)
    total = total + recargo_fin_de_semana(dia)
    total = descuento_cliente(total, cliente)
    total = aplicar_cupon(total, cupon)
    total = max(total, COSTO_MINIMO)
    return redondear_a_cien(total)