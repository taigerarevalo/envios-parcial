# Parte 8 · Solicitud de cambio y análisis de impacto

## 1. Solicitud de cambio asignada

Con mis parámetros, A = 4 y F = 1, entonces (A + F) mod 3 = 5 mod 3 = **2**.

**Solicitud de cambio 2, hora pico:** se agrega el parámetro `hora` (de 0 a 23). Entre las 17 y las 19, inclusive, hay un recargo del 8 %, que se calcula después del recargo por zona.

## 2. Análisis de impacto

### 2.1 Requisito nuevo

- **R9. Hora pico.** Si la hora está entre 17 y 19, ambas inclusive, se suma un 8 % al valor ya con el recargo de zona. Una hora fuera del rango de 0 a 23 lanza un error.

### 2.2 Elementos afectados

| Elemento | ¿Se afecta? | Detalle |
|---|---|---|
| R1 (peso) | No | Sin cambios |
| R2 (validación) | Sí, se amplía | También se valida que la hora esté entre 0 y 23 |
| R3 (tarifa base) | No | Sin cambios |
| R4 (zona) | Sí, por orden | El 8 % se calcula sobre el valor que ya tiene el recargo de zona |
| R5 (fin de semana) | No | Sigue después de la hora pico |
| R6 (descuentos) | No | Reciben un valor distinto, pero su regla no cambia |
| R7 (cupón) | No | Sin cambios |
| R8 (mínimo y redondeo) | No | Sin cambios |

### 2.3 Historias de usuario

- **HU-1 (validación):** se afecta, porque ahora valida también la hora.
- **HU-2 (tarifa):** se afecta, porque el cálculo cambia en hora pico.
- **HU-3 (descuentos y redondeo):** no se afecta.
- **HU-4 (nueva):** hora pico.

**HU-4.** Como operador de EnvíaYa, quiero que los envíos en hora pico lleven un recargo para cubrir la mayor demanda.

- **Dado** 5 kg, zona urbana, cliente normal, día 2 y hora 17, **cuando** calculo el costo, **entonces** 9.000 × 1,08 = 9.720 y el resultado es $9.700.
- **Dado** la misma entrada con hora 16, **cuando** calculo el costo, **entonces** el resultado es $9.000.
- **Dado** una hora 24 o -1, **cuando** calculo el costo, **entonces** se lanza un error.

### 2.4 Matriz de trazabilidad actualizada

| Requisito | Historia | Casos de prueba |
|---|---|---|
| R1 | HU-1 | CP-07, CP-12, test_peso_sobre_maximo |
| R2 | HU-1 | CP-13, CP-14, HP-08, HP-09 |
| R3 | HU-2 | CP-08, CP-09, CP-10, CP-11, CP-19 |
| R4 | HU-2 | CP-02, CP-15, CP-20 |
| R5 | HU-2 | CP-03, CP-16 |
| R6 | HU-3 | CP-04, CP-05, CP-17, CP-18 |
| R7 | HU-1 | test_cupon_inexistente_es_error |
| R8 | HU-3 | CP-06, CP-21 |
| **R9 (nuevo)** | **HU-4** | **HP-01 a HP-09** |

### 2.5 Partes del código afectadas

- `calc`: recibe el parámetro nuevo `hora` y llama a la función de hora pico después de la zona.
- `validar_entradas`: valida el rango de la hora.
- Función nueva `recargo_hora_pico`.
- Constantes nuevas: `HORA_MINIMA`, `HORA_MAXIMA`, `HORA_PICO_INICIO`, `HORA_PICO_FIN` y `RECARGO_HORA_PICO`.
- Pruebas: los 23 casos existentes no cambian y se agregan 9 casos nuevos.

## 3. Tipo de mantenimiento

**Perfectivo.** El cambio agrega una funcionalidad nueva que pidió el negocio. No corrige un defecto (correctivo), no responde a un cambio del entorno (adaptativo) y no es una mejora interna de la estructura (preventivo).

## 4. Pruebas escritas primero

Antes de tocar el código se escribieron los casos de hora pico en la rama `feat/hora-pico`. Los resultados esperados se calcularon a mano.

| ID | Entradas (peso, zona, cliente, día, cupón, hora) | Cálculo a mano | Esperado |
|---|---|---|---|
| HP-01 | 5, urbana, normal, 2, -, 17 | 9.000 × 1,08 = 9.720 | $9.700 |
| HP-02 | 5, urbana, normal, 2, -, 19 | 9.000 × 1,08 = 9.720 | $9.700 |
| HP-03 | 5, urbana, normal, 2, -, 16 | sin recargo | $9.000 |
| HP-04 | 5, urbana, normal, 2, -, 20 | sin recargo | $9.000 |
| HP-05 | 5, rural, vip, 6, -, 18 | 9.000 × 1,10 = 9.900; × 1,08 = 10.692; + 2.000 = 12.692; × 0,85 = 10.788,20 | $10.800 |
| HP-06 | 5, urbana, normal, 2, -, 0 | sin recargo | $9.000 |
| HP-07 | 5, urbana, normal, 2, -, 23 | sin recargo | $9.000 |
| HP-08 | 5, urbana, normal, 2, -, 24 | hora fuera de rango | error |
| HP-09 | 5, urbana, normal, 2, -, -1 | hora fuera de rango | error |

**Técnica:** valores límite (16, 17, 19 y 20 alrededor de la franja; 0 y 23 en los extremos válidos; -1 y 24 fuera de rango) y partición de equivalencia.

**Ejecución antes de implementar:** 9 failed, 23 passed. Fallan porque `calc` todavía no acepta el parámetro `hora`. Evidencia: Anexo, Figura 7.

## 5. Implementación

Se hizo en la rama `feat/hora-pico`.

```python
HORA_MINIMA = 0
HORA_MAXIMA = 23
HORA_PICO_INICIO = 17
HORA_PICO_FIN = 19
RECARGO_HORA_PICO = 0.08


def recargo_hora_pico(valor, hora):
    if hora is not None and HORA_PICO_INICIO <= hora <= HORA_PICO_FIN:
        return valor + valor * RECARGO_HORA_PICO
    return valor


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
```

`validar_entradas` recibe también la hora y lanza `ValueError("hora invalida")` si está fuera de 0 a 23.

**Decisión de diseño:** el recargo de hora pico se calcula sobre el valor con el recargo de zona y antes de sumar el recargo fijo de fin de semana, de acuerdo con el enunciado ("después del recargo por zona").

## 6. Regresión

Resultado después de implementar: **32 passed**, con 100 % de cobertura de sentencias y de ramas. Evidencia: Anexo, Figura 8.

## 7. Nueva versión: v2.1.0

El parámetro `hora` es **opcional** (`hora=None`). Las llamadas que ya existían siguen funcionando igual, así que el cambio es compatible hacia atrás y solo agrega funcionalidad. Según el versionado semántico eso sube el número **MINOR**: de 2.0.0 a **2.1.0**. Si `hora` fuera obligatorio, rompería las llamadas anteriores y la versión sería 3.0.0.

Entrada agregada al `CHANGELOG.md`:

```markdown
## [2.1.0] - 2026-11-11

### Agregado
- Parámetro opcional `hora` en `calc` (0 a 23). Entre las 17 y las 19, inclusive, se aplica un recargo del 8 % después del recargo por zona (R9).
- Validación de la hora: un valor fuera de 0 a 23 lanza `ValueError`.
- 9 casos de prueba nuevos (HP-01 a HP-09).
```

Etiqueta publicada: `v2.1.0`.