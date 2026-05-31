"""
indicadores.py
==============
Módulo de indicadores de desempeño (KPIs) para el estado hídrico del suelo.
Implementa el sistema de clasificación tipo semáforo
(Verde / Amarillo / Rojo) para decisiones de riego.

Funciones:
    calcular_kpi_potencial()   -- KPI 1: potencial mátrico promedio (kPa)
    calcular_kpi_variabilidad()-- KPI 2: coeficiente de variación entre sensores
    calcular_kpi_tendencia()   -- KPI 3: tasa de cambio temporal del potencial
    clasificar_semaforo()      -- asigna Verde/Amarillo/Rojo según umbrales
    resumen_indicadores()      -- tabla consolidada de todos los KPIs

Desarrollado en: 03_POO_indicadores.ipynb
"""