"""
sensores.py
===========
Módulo de Programación Orientada a Objetos.
Define la jerarquía de clases para representar sensores de suelo,
mediciones y parcelas agrícolas.

Clases:
    Sensor            -- clase base abstracta
    SensorResistivo   -- sensores basados en resistencia eléctrica (Watermark)
    SensorTDR         -- sensores de reflectometría en dominio del tiempo
    SensorCapacitivo  -- sensores capacitivos (5TM, 10HS)
    SensorTensiometro -- tensiómetros de referencia
    Medicion          -- registro individual de una lectura
    Parcela           -- colección de sensores en una ubicación

Desarrollado en: 03_POO_indicadores.ipynb
"""