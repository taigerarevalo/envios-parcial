# Parte 5 - Defectos

## 1. Diagnóstico inicial
La versión heredada del código presentaba varios defectos de validación y lógica de cálculo. El objetivo del análisis fue detectar fallas antes de refactorizar y confirmar que cada una quedaba corregida por la suite final.

## 2. Defectos identificados

### DEF-01: no se cobraba recargo el sábado
- Requisito afectado: R5.
- Caso reproducible: `calc(3, "urbana", "normal", 6)`.
- Error: la condición solo contemplaba el domingo y no sabado.
- Impacto: el cobro del envío era menor al esperado.

### DEF-02: el redondeo truncaba los valores
- Requisito afectado: R8.
- Error: el cálculo descartaba los decimales en vez de redondear al valor más cercano de $100.
- Impacto: los montos siempre quedaban por debajo del valor correcto.

### DEF-03: cupones inexistentes se ignoraban
- Requisito afectado: R7.
- Error: si el cupón no era válido, el sistema calculaba igual sin error.
- Impacto: se aceptaban descuentos inexistentes.

### DEF-04: la zona no se validaba
- Requisito afectado: R2.
- Error: cualquier valor de zona era aceptado.
- Impacto: se podía cotizar un envío a una zona no soportada.

### DEF-05: el día no se validaba
- Requisito afectado: R2.
- Error: días fuera del rango 1 a 7 se aceptaban.
- Impacto: se podía calcular un envío con un día no válido.

## 3. Evidencia de ejecución
La suite heredada fallaba en 10 de 22 casos. Tras la refactorización, se corrigieron esos defectos y la suite quedó estable con 32 casos aprobados.

## 4. Conclusión
La detección de defectos permitió corregir errores reales de negocio y mejorar la confiabilidad del cálculo del envío. La solución final incorpora validaciones formales, testeo automatizado y cobertura completa.

