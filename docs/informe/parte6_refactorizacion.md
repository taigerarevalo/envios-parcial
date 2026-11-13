# Parte 6 - Refactorización

## 1. Objetivo
La refactorización busca modernizar el código heredado sin cambiar la intención del negocio. Se prioriza la claridad, la reutilización, la validación y la facilidad de mantenimiento.

## 2. Cambios principales
### 2.1 Extracción de funciones
Se separaron responsabilidades en funciones independientes:
- `validar_entradas`
- `tarifa_base`
- `recargo_fin_de_semana`
- `recargo_hora_pico`
- `descuento_cliente`
- `aplicar_cupon`
- `redondear_a_cien`

### 2.2 Eliminación de números mágicos
Los valores fijos del dominio se reemplazaron por constantes con nombres descriptivos, por ejemplo:
- `PESO_MAXIMO`
- `DIA_MINIMO`
- `DIA_MAXIMO`
- `RECARGO_HORA_PICO`
- `COSTO_MINIMO`

### 2.3 Introducción del patrón Estrategia
Las zonas geográficas fueron modeladas con clases que aplican un recargo específico:
- `ZonaUrbana`
- `ZonaRural`
- `ZonaNacional`

Esto evita condicionales gigantes y hace más fácil ampliar nuevas zonas en el futuro.

### 2.4 Mejora del contrato de la función
La función `calc` quedó con parámetros descriptivos y con validación explícita. Además, ya no imprime resultados por pantalla ni depende de un parámetro `flag` obsoleto.

## 3. Beneficios obtenidos
- Código más legible.
- Menor riesgo de regresiones.
- Mejor testabilidad.
- Validación más robusta.
- Sustentabilidad del proyecto a largo plazo.

## 4. Resultado final
La refactorización permitió mantener la lógica de negocio original y al mismo tiempo corregir defectos y reforzar la calidad del software.
