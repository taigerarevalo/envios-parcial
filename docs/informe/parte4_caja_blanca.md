# Parte 4 - Caja blanca

## 1. Enfoque
La prueba de caja blanca revisa las decisiones internas del código, las condiciones, las ramas y los flujos de ejecución. Se valida que cada comprobación del programa se corresponda con una regla del negocio.

## 2. Rutas críticas analizadas
### 2.1 Validación de entradas
La función `validar_entradas` comprueba:
- peso positivo y no superior a 50;
- zona válida;
- día válido;
- hora válida si existe.

Si alguna condición falla, se lanza `ValueError`.

### 2.2 Cálculo de tarifa base
La función `tarifa_base` divide el cálculo en tramos:
- hasta 3 kg, tarifa 6.000;
- hasta 10 kg, tarifa 9.000;
- superior a 10 kg, suma tarifa base más costo adicional por kilogramo.

### 2.3 Estrategia por zona
Se usa una estructura por estrategia:
- `ZonaUrbana.aplicar`: sin incremento;
- `ZonaRural.aplicar`: agrega 10 %;
- `ZonaNacional.aplicar`: agrega 45 %.

### 2.4 Descuentos y cupones
- `descuento_cliente` aplica descuento por cliente.
- `aplicar_cupon` valida cupón existente y aplica el 10 %.
- Si el cupón no es válido, se lanza excepción.

### 2.5 Redondeo de salida
La función `redondear_a_cien` redondea al múltiplo de 100 más cercano para garantizar el formato de cobro esperado.

## 3. Cobertura de ramas
El flujo del código tiene ramas de validación, cálculo, descuentos, cupones, recargo por día y recargo por hora pico. Cada rama se cubre con pruebas unitarias específicas para evitar regresiones.

## 4. Conclusión
La revisión de caja blanca confirma que la lógica es consistente, ordenada y alineada con los requisitos. La separación en funciones y constantes ayuda a la mantenibilidad y a la prueba aislada de cada comportamiento.
