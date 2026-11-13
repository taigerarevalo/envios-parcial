# Parte 7 - Configuración

## 1. Entorno de trabajo
El proyecto se desarrolla en Python y utiliza un entorno virtual para evitar interferencias con librerías del sistema.

## 2. Dependencias
Las dependencias principales son:
- pytest: ejecución de pruebas automatizadas.
- coverage: cálculo de cobertura de pruebas.

El archivo de dependencias se encuentra en [requirements.txt](../..\requirements.txt).

## 3. Estructura del repositorio
- `.venv/`: entorno virtual.
- `.gitignore`: exclusión de archivos temporales.
- `README.md`: documentación base del proyecto.
- `CHANGELOG.md`: historial de cambios.
- `envios.py`: código principal.
- `test_envios.py`: suite de pruebas.
- `docs/`: documentación del parcial.

## 4. Recomendaciones de ejecución
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## 5. Conclusión
La configuración del proyecto permite una ejecución reproducible, una validación consistente y una estructura ordenada para la entrega final del parcial.
