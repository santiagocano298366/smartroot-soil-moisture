"""
simulacion.py
=============
Módulo de simulación de escenarios e incertidumbre.
Implementa la simulación de Monte Carlo para cuantificar
la incertidumbre de medición de los electrodos de bajo costo
y su efecto sobre la estimación del potencial mátrico.

Funciones:
    montecarlo_resistividad()  -- simula ruido de medición (>= 1000 iter)
    simular_escenarios()       -- escenarios: seco / normal / húmedo
    calcular_probabilidad()    -- P(ψ < umbral_riego)
    resumen_montecarlo()       -- estadísticos e intervalos de confianza

Desarrollado en: 04_simulacion_montecarlo.ipynb

Autor:     Santiago Cano Molina
Perfil:    Ingeniero Mecatrónico · Maestría en Automatización y Control Industrial
Proyecto:  SmartRoot — Fundamentos de Programación Científica · Posgrado 2026-1
"""