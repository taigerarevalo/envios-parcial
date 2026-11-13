# Envíos Parcial

Este proyecto tiene como objetivo analizar, refactorizar y validar un sistema de cálculo de costos de envío. La base del trabajo consiste en un módulo heredado que debe corregirse y documentarse siguiendo una metodología de pruebas, diagnóstico de defectos y mejora continua.

## Descripción general

La aplicación calcula el costo de un envío a partir de distintos factores como:
- peso del paquete;
- zona del envío (urbana, rural o nacional);
- tipo de cliente;
- día de envío;
- cupones promocionales;
- hora pico;
- redondeo final y costo mínimo.

El propósito del parcial es mostrar cómo se debe trabajar con software heredado: identificar requisitos, diseñar pruebas, detectar errores, aplicar refactorización y documentar el proceso completo.

## Estructura del proyecto

- `.gitignore`: ignora archivos temporales y el entorno virtual.
- `envios.py`: módulo principal con la lógica heredada del cálculo.
- `test_envios.py`: pruebas unitarias con `pytest`.
- `CHANGELOG.md`: historial de cambios y versiones del proyecto.
- `docs/informe/`: entregables del análisis del parcial.
- `docs/capturas/`: evidencias visuales de pruebas y cobertura.
- `requirements.txt`: dependencias del proyecto.

## Requisitos de ejecución

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas

```bash
pytest -q
```

## Simulador del controlador de aerogenerador

La página interactiva de `site/` representa la máquina de estados del controlador mostrada en el diagrama de la entrega. Permite aplicar las señales `VB`, `VN`, `VF`, `FALLA` y `RESET`, revisar las salidas de cada estado y recorrer secuencias de ejemplo. Es una demostración independiente del módulo de cálculo de envíos.

Para abrirla localmente, ejecuta desde la raíz del proyecto:

```bash
python -m http.server 8000 --directory site
```

Luego visita `http://localhost:8000`. La página no requiere instalar dependencias.

## Objetivo pedagógico

Este repositorio sirve como ejemplo de:
- análisis de requisitos;
- validación de comportamiento mediante pruebas;
- detección de defectos reales;
- refactorización de código heredado;
- documentación técnica y de cambios;
- preparación para una entrega final del trabajo práctico.

## Estado esperado

El proyecto se considera correcto cuando:
- la suite de pruebas pasa sin fallos;
- la lógica de cálculo cumple con los requisitos del parcial;
- los defectos fueron corregidos y documentados;
- la estructura del repositorio coincide con la propuesta del enunciado.

