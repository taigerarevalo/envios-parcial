# Parte 2 - Plan de pruebas

## 1. Objetivo
El plan de pruebas tiene como finalidad verificar que la función `calc` cumple los requisitos funcionales del sistema, tanto en casos normales como en condiciones límite y de error.

## 2. Tipo de pruebas
Se aplican pruebas unitarias sobre la función principal y sobre las funciones auxiliares que componen la lógica de cálculo.

### 2.1 Pruebas de caja negra
Se evalúa la salida del sistema a partir de entradas conocidas, sin depender de la implementación interna.

### 2.2 Pruebas de caja blanca
Se revisan las ramas, condicionales y validaciones del código para asegurar que cada decisión se comporta correctamente.

## 3. Casos de prueba previstos
Se diseñan pruebas para:

- pesos válidos e inválidos;
- zonas válidas e inválidas;
- días válidos e inválidos;
- clientes frecuentes, VIP y normales;
- cupones válidos e inválidos;
- hora pico y fuera de pico;
- redondeo al múltiplo de $100;
- costo mínimo.

## 4. Criterios de entrada y salida
### Entradas válidas
- Peso entre 0 y 50, excluyendo 0.
- Zona entre urbana, rural y nacional.
- Día entre 1 y 7.
- Hora entre 0 y 23 si se especifica.

### Salidas esperadas
- El resultado debe ser un número entero múltiplo de 100.
- Si la entrada es inválida, la función debe lanzar `ValueError`.
- Si la entrada es válida, debe devolver el costo final del envío.

## 5. Herramientas
- Python 3.x
- pytest para automatización de pruebas
- coverage para medición de cobertura

## 6. Estructura de la suite
La suite de pruebas incluye:

- casos de cálculo normal;
- validación de errores;
- pruebas específicas de hora pico;
- pruebas de redondeo y de descuentos;
- casos de borde y combinaciones de parámetros.

## 7. Resultado esperado
La prueba final debe garantizar que el sistema cumpla con los requisitos y que no existan fallos en el cálculo ni en la validación de entradas.
