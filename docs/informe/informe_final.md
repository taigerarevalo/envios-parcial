# Informe final del parcial - Proyecto Envios

## Resumen ejecutivo
Este proyecto tuvo como objetivo analizar, corregir y documentar una función de cálculo de envíos heredada. El trabajo se dividió en seis grandes etapas: análisis de requisitos, planificación de pruebas, pruebas de caja negra, pruebas de caja blanca, detección de defectos, refactorización y documentación del cambio.

La solución final incluye:
- validación de entradas;
- cálculo de tarifa según peso y zona;
- descuentos por tipo de cliente;
- cupones promocionales;
- recargo por fin de semana;
- recargo por hora pico;
- redondeo al múltiplo de $100 más cercano;
- pruebas automatizadas con pytest.

## 1. Requisitos
Los requisitos funcionales y no funcionales se detallan en [parte1_requisitos.md](parte1_requisitos.md).

## 2. Plan de pruebas
Se diseñó una suite de pruebas enfocada en:
- casos normales;
- casos límite;
- casos de error;
- combinaciones de parámetros;
- validación de rangos y errores controlados.

El plan completo está en [parte2_plan_pruebas.md](parte2_plan_pruebas.md).

## 3. Caja negra
Se validó el comportamiento observable de la función sin depender de la implementación interna. Se aplicaron particiones y casos límite para comprobar que la salida coincida con el negocio esperado.

Ver [parte3_caja_negra.md](parte3_caja_negra.md).

## 4. Caja blanca
Se revisaron las ramas, validaciones y funciones internas del cálculo. Se confirmó que cada condicional correspondía a una regla explícita del sistema.

Ver [parte4_caja_blanca.md](parte4_caja_blanca.md).

## 5. Defectos
Durante la ejecución inicial del código heredado se detectaron varios fallos reales de lógica y validación, por ejemplo:
- no se cobraba el sábado;
- el redondeo truncaba valores;
- cupones inválidos no generaban error;
- zonas y días no se validaban.

La documentación completa se encuentra en [parte5_defectos.md](parte5_defectos.md).

## 6. Refactorización
El código se mejoró para hacer más clara la responsabilidad de cada función y eliminar valores mágicos. Se usaron constantes con nombre y una estrategia por zona para mantener el código legible y extensible.

Ver [parte6_refactorizacion.md](parte6_refactorizacion.md).

## 7. Configuración
El proyecto quedó configurado con Python, pytest y coverage, además de una estructura de repositorio ordenada y reproducible.

Ver [parte7_configuracion.md](parte7_configuracion.md).

## 8. Cambio solicitado
La nueva solicitud fue agregar el parámetro `hora` para cubrir la franja de hora pico. El cambio se documenta con su impacto, trazabilidad, pruebas de regresión y versión final del software.

Ver [parte8_cambio.md](parte8_cambio.md).

## 9. Resultado final verificado
Se ejecutó la suite completa con pytest y el proyecto quedó validado con éxito.

Comando ejecutado:

```bash
cd "C:\Users\JUAN PC\Documents\envios-parcial"; .\.venv\Scripts\python -m pytest -q
```

Resultado verificado:

```text
32 passed in 0.16s
```

## 10. Conclusión
El parcial quedó resuelto en forma completa: el código fue analizado, corregido, refactorizado, probado y documentado. El proyecto final se encuentra listo para su entrega y revisión.
