# Parte 3 - Caja negra

## 1. Enfoque metodológico
La estrategia de caja negra consiste en verificar la salida del sistema sin depender del código interno. Se validan solamente las entradas y los resultados observables.

## 2. Equivalencias y particiones
### 2.1 Peso
- Peso válido: valores mayores que 0 y menores o iguales a 50.
- Peso inválido: 0, negativos y mayores a 50.

### 2.2 Zona
- Zonas válidas: urbana, rural, nacional.
- Zona inválida: cualquier otro valor.

### 2.3 Día
- Días válidos: 1 a 7.
- Día inválido: fuera de este rango.

### 2.4 Hora
- Hora válida: 0 a 23.
- Hora inválida: negativa o mayor que 23.

### 2.5 Cliente
- Normal, frecuente, vip.

### 2.6 Cupón
- Cupón válido: `ENVIO10`.
- Cupón inválido: cualquier otro valor distinto de `ENVIO10`.

## 3. Casos de prueba significativos
- `calc(3, "urbana", "normal", 2)` → costo esperado de 6.000.
- `calc(3, "urbana", "normal", 6)` → incluye recargo por fin de semana.
- `calc(5, "rural", "vip", 5)` → aplica zona rural y descuento VIP.
- `calc(5, "urbana", "normal", 2, None, 17)` → incluye hora pico.
- `calc(0, "urbana", "normal", 2)` → lanza `ValueError`.
- `calc(5, "aerea", "normal", 2)` → lanza `ValueError`.
- `calc(5, "urbana", "normal", 8)` → lanza `ValueError`.
- `calc(5, "urbana", "normal", 2, "PROMO5")` → lanza `ValueError`.

## 4. Conclusión
La caja negra confirma que la función cumple con los requisitos esperados desde la perspectiva del usuario y que los errores se manejan de forma controlada.
