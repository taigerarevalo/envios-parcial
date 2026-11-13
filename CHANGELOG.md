# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

## [Sin publicar]

## [2.0.0] - 2026-11-11

### Cambiado
- **BREAKING:** se elimina el parámetro `flag` de `calc`. Ya no imprime el costo por pantalla.
- Se extraen funciones: `validar_entradas`, `tarifa_base`, `recargo_fin_de_semana`, `descuento_cliente`, `aplicar_cupon` y `redondear_a_cien`.
- Los números mágicos pasan a constantes con nombre.
- Las zonas se implementan con el patrón Estrategia.
- Los parámetros de `calc` pasan a nombres descriptivos.

### Corregido
- DEF-01: el recargo de fin de semana no se cobraba el sábado (R5).
- DEF-02: el redondeo truncaba en vez de redondear al $100 más cercano (R8).
- DEF-03: un cupón inexistente se ignoraba; ahora lanza error (R7).
- DEF-04: una zona inválida no lanzaba error (R2).
- DEF-05: un día fuera del rango 1 a 7 no lanzaba error (R2).

### Agregado
- Suite de pruebas con pytest (23 casos) y 100 % de cobertura.

## [1.0.0] - 2026-11-11

### Agregado
- Versión heredada de `calc` con la configuración del estudiante.

[Sin publicar]: https://github.com/taigerarevalo/envios-parcial/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/taigerarevalo/envios-parcial/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/taigerarevalo/envios-parcial/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/taigerarevalo/envios-parcial/releases/tag/v1.0.0
## [2.1.0] - 2026-11-11

### Agregado
- Parámetro opcional `hora` en `calc` (0 a 23). Entre las 17 y las 19, inclusive, se aplica un recargo del 8 % después del recargo por zona (R9).
- Validación de la hora: un valor fuera de 0 a 23 lanza `ValueError`.
- 9 casos de prueba nuevos (HP-01 a HP-09).