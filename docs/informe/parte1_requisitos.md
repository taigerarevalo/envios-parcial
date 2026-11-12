# Parte 1 - Requisitos

## 1. Objetivo del sistema
El sistema debe calcular el costo de un envío a partir de las características del paquete, la zona geográfica, el tipo de cliente, el día de envío y otros condicionantes comerciales. La funcionalidad central se encapsula en la función `calc`, la cual debe devolver el valor final del envío ya validado y ajustado por descuentos, recargos y redondeo.

## 2. Alcance funcional
Se requieren las siguientes capacidades:

- Definir el peso del paquete y validar que esté dentro del rango aceptado.
- Identificar la zona del envío: urbana, rural o nacional.
- Aplicar la tarifa base según el peso del paquete.
- Ajustar el precio por recargos dependientes del día y de la hora pico.
- Aplicar descuentos según el tipo de cliente.
- Aplicar cupones promocionales cuando existan.
- Redondear el total final al múltiplo de $100 más cercano.
- Generar errores controlados si la entrada es inválida.

## 3. Requisitos funcionales clave
### RF-01: Validación de peso
El peso debe ser mayor que 0 y no superior a 50 kg.

### RF-02: Validación de zona
La zona debe ser una de las permitidas: urbana, rural o nacional.

### RF-03: Validación del día
El día debe estar comprendido entre 1 y 7, donde 1 corresponde al lunes y 7 al domingo.

### RF-04: Validación de la hora
Si se recibe la hora, debe estar entre 0 y 23 inclusive.

### RF-05: Tarifa base
La tarifa base depende del peso. Para pesos menores o iguales a 3 kg se usa el tramo 1; para pesos hasta 10 kg se usa el tramo 2; y para pesos mayores se aplica el tramo 2 más un costo extra por kilogramo adicional.

### RF-06: Recargo por zona
- Urbana: sin recargo.
- Rural: recargo del 10 %.
- Nacional: recargo del 45 %.

### RF-07: Recargo por fin de semana
Si el envío se realiza el sábado o domingo, se agrega un recargo fijo de $2.000.

### RF-08: Descuentos por cliente
- Frecuente: 5 % de descuento.
- VIP: 15 % de descuento.
- Normal: sin descuento.

### RF-09: Cupón promocional
Si el cupón es `ENVIO10`, se aplica un descuento del 10 %. Si el cupón no existe, se lanza error.

### RF-10: Hora pico
Entre las 17 y las 19 inclusive, se aplica un recargo del 8 % sobre el subtotal ya ajustado por zona.

### RF-11: Redondeo
El precio final debe redondearse al $100 más cercano.

### RF-12: Costo mínimo
El costo final nunca puede ser inferior a $5.000.

## 4. Requisitos no funcionales
- El código debe ser legible y mantenible.
- La lógica debe estar dividida en funciones pequeñas y claras.
- Deben existir pruebas automatizadas que validen comportamiento.
- La solución debe evitar valores mágicos y usar constantes con nombre.
- Se debe documentar el historial de cambios y los defectos corregidos.

## 5. Restricciones del proyecto
- El proyecto se implementa en Python.
- La verificación se realiza con pytest.
- La cobertura de pruebas debe ser máxima o cercana al 100 %.
- La entrega final debe incluir documentación de requisitos, análisis, defectos y refactorización.
