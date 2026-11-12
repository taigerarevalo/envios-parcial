# Parte 5 · Automatización, ejecución y defectos

## Ejecución contra el código heredado (v1.0.0)

Resultado: 22 casos, **10 fallidos y 12 aprobados**.
Evidencia: `docs/capturas/pruebas_fallando.png`

## Reporte de defectos

### DEF-01 · No se cobra el recargo de fin de semana el sábado
- **Requisito que incumple:** R5
- **Pasos para reproducir:** `calc(3, "urbana", "normal", 6)`
- **Resultado esperado:** 8.000
- **Resultado obtenido:** 6.000
- **Severidad:** Alta. Se cobra $2.000 menos en todos los envíos del sábado.
- **Prioridad:** Alta. Hay pérdida de dinero en cada envío afectado.
- **Causa:** la condición `d > 6` solo incluye el domingo.
- **Casos que lo detectan:** CP-01, CP-03

### DEF-02 · El redondeo trunca en vez de redondear al $100 más cercano
- **Requisito que incumple:** R8
- **Pasos para reproducir:** `calc(5, "urbana", "frecuente", 2)`
- **Resultado esperado:** 8.600
- **Resultado obtenido:** 8.500
- **Severidad:** Media. El error es de hasta $99 por envío.
- **Prioridad:** Alta. Afecta a casi todos los cálculos.
- **Causa:** `int(t / 100) * 100` descarta los decimales.
- **Casos que lo detectan:** CP-01, CP-02, CP-06, CP-15, CP-17, CP-18

### DEF-03 · Un cupón inexistente se ignora en vez de lanzar error
- **Requisito que incumple:** R7
- **Pasos para reproducir:** `calc(3, "urbana", "normal", 2, "PROMO5")`
- **Resultado esperado:** ValueError
- **Resultado obtenido:** calcula sin error
- **Severidad:** Media. El cliente cree que tiene un descuento que no existe.
- **Prioridad:** Media.
- **Causa:** el `if cup == "ENVIO10"` no tiene un `else` que lance el error.
- **Casos que lo detectan:** `test_cupon_inexistente_es_error`

### DEF-04 · No se valida la zona
- **Requisito que incumple:** R2
- **Pasos para reproducir:** `calc(5, "aerea", "normal", 2)`
- **Resultado esperado:** ValueError
- **Resultado obtenido:** calcula sin error
- **Severidad:** Media. Se cotiza un envío a una zona que no existe.
- **Prioridad:** Media.
- **Causa:** la cadena `if/elif` de zonas no tiene `else`.
- **Casos que lo detectan:** CP-13

### DEF-05 · No se valida el día
- **Requisito que incumple:** R2
- **Pasos para reproducir:** `calc(5, "urbana", "normal", 8)`
- **Resultado esperado:** ValueError
- **Resultado obtenido:** calcula sin error (y cobra recargo de fin de semana)
- **Severidad:** Media.
- **Prioridad:** Media.
- **Causa:** no hay validación del rango 1 a 7.
- **Casos que lo detectan:** CP-14

## Métricas

| Métrica | Valor |
|---|---|
| Casos ejecutados | 22 |
| Casos que pasan | 12 (54,5 %) |
| Casos que fallan | 10 (45,5 %) |
| Defectos Alta / Media / Baja | 1 / 4 / 0 |
| Densidad de defectos | 5 defectos ÷ 42 líneas × 100 ≈ 11,9 por cada 100 líneas |
| Cobertura de sentencias | 93,1 % (27 de 29; sin cubrir las líneas 39 y 41) |
| Cobertura de ramas | 92,3 % (24 de 26; sin cubrir `t < 5000` y `flag`) |

