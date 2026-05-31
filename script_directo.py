import numpy as np
import os
import sys

# Redirigir salida estándar a archivo
os.makedirs('outputs', exist_ok=True)

with open('outputs/06_resultados_ejecucion.txt', 'w', encoding='utf-8') as f:
    sys.stdout = f

    class Cuadrilla:
        def __init__(self, id_cuadrilla, zona_base, capacidad_diaria_horas):
            self.id_cuadrilla = id_cuadrilla
            self.zona_base = zona_base
            self.capacidad_diaria_horas = capacidad_diaria_horas
            self.ordenes_asignadas = []
        
        def horas_asignadas(self):
            return sum(ot.duracion_estimada for ot in self.ordenes_asignadas)
        
        def disponibilidad(self):
            return self.capacidad_diaria_horas - self.horas_asignadas()
        
        def asignar_ot(self, ot):
            if ot.estado != 'Pendiente':
                print(f'❌ La OT {ot.id_ot} no está Pendiente.')
                return False
                
            if self.disponibilidad() >= ot.duracion_estimada:
                self.ordenes_asignadas.append(ot)
                ot.estado = 'Asignada'
                print(f'✅ OT {ot.id_ot} asignada a cuadrilla {self.id_cuadrilla}. Disponibilidad restante: {self.disponibilidad()}h')
                return True
            else:
                print(f'⚠️ Cuadrilla {self.id_cuadrilla} sin capacidad para OT {ot.id_ot} (Requiere {ot.duracion_estimada}h, disponible {self.disponibilidad()}h)')
                return False
                
        def mostrar_programacion(self):
            print(f'\n📅 Programación Cuadrilla {self.id_cuadrilla} (Zona: {self.zona_base})')
            print(f'   Horas capacidad: {self.capacidad_diaria_horas} | Asignadas: {self.horas_asignadas()}')
            print('   ' + '-'*50)
            for ot in sorted(self.ordenes_asignadas, key=lambda x: x.prioridad):
                print(f'   - [{ot.id_ot}] {ot.tipo_ot()} | Prio: {ot.prioridad} | {ot.duracion_estimada}h | ANS: {ot.ans_horas}h')
            print('   ' + '-'*50)

    from abc import ABC, abstractmethod

    class OrdenTrabajo(ABC):
        def __init__(self, id_ot, zona, duracion_estimada, prioridad, ans_horas):
            self.id_ot = id_ot
            self.zona = zona
            self.duracion_estimada = duracion_estimada
            self.prioridad = prioridad
            self.ans_horas = ans_horas
            self.estado = 'Pendiente'
            
        @abstractmethod
        def tipo_ot(self):
            pass

        @abstractmethod
        def calcular_costo(self, costo_hora_base):
            pass

    class OT_Mantenimiento(OrdenTrabajo):
        def tipo_ot(self):
            return 'Mantenimiento Preventivo'
            
        def calcular_costo(self, costo_hora_base):
            return (self.duracion_estimada * costo_hora_base) + 15

    class OT_Urgente(OrdenTrabajo):
        def tipo_ot(self):
            return 'Riego Urgente / Crítica'
            
        def calcular_costo(self, costo_hora_base):
            return self.duracion_estimada * (costo_hora_base * 1.5)
            
    class OT_Instalacion(OrdenTrabajo):
        def __init__(self, id_ot, zona, duracion_estimada, prioridad, ans_horas, costo_equipos):
            super().__init__(id_ot, zona, duracion_estimada, prioridad, ans_horas)
            self.costo_equipos = costo_equipos
            
        def tipo_ot(self):
            return 'Instalación Equipos'
            
        def calcular_costo(self, costo_hora_base):
            return (self.duracion_estimada * costo_hora_base * 1.2) + self.costo_equipos

    cuadrilla_A = Cuadrilla('C-Alfa', zona_base='Sector Norte', capacidad_diaria_horas=8.0)
    cuadrilla_B = Cuadrilla('C-Beta', zona_base='Sector Sur', capacidad_diaria_horas=6.0)
    cuadrillas = [cuadrilla_A, cuadrilla_B]

    lista_ots = [
        OT_Mantenimiento('OT-001', 'Sector Norte', duracion_estimada=2.0, prioridad=3, ans_horas=48),
        OT_Urgente('OT-002', 'Sector Norte', duracion_estimada=3.5, prioridad=1, ans_horas=4),
        OT_Instalacion('OT-003', 'Sector Sur', duracion_estimada=4.0, prioridad=2, ans_horas=24, costo_equipos=25.0),
        OT_Urgente('OT-004', 'Sector Sur', duracion_estimada=2.0, prioridad=1, ans_horas=3),
        OT_Mantenimiento('OT-005', 'Sector Sur', duracion_estimada=3.0, prioridad=3, ans_horas=72)
    ]

    ots_priorizadas = sorted(lista_ots, key=lambda x: (x.prioridad, x.ans_horas))

    print('⚙️ ASIGNACIÓN AUTOMÁTICA DE OTs')
    print('='*50)
    for ot in ots_priorizadas:
        cuadrilla_ideal = next((c for c in cuadrillas if c.zona_base == ot.zona and c.disponibilidad() >= ot.duracion_estimada), None)
        if not cuadrilla_ideal:
            cuadrilla_ideal = next((c for c in cuadrillas if c.disponibilidad() >= ot.duracion_estimada), None)
            
        if cuadrilla_ideal:
            cuadrilla_ideal.asignar_ot(ot)
        else:
            print(f'🚨 ALERTA: No hay cuadrillas con capacidad para la OT {ot.id_ot} (Prioridad {ot.prioridad})')

    print('\n📋 RESULTADO DE LA PROGRAMACIÓN')
    for c in cuadrillas:
        c.mostrar_programacion()

    print('\n💰 ANÁLISIS DE COSTOS (Demostración de Polimorfismo)')
    print('='*50)
    costo_hora = 20.0
    costo_total = 0
    for ot in lista_ots:
        costo = ot.calcular_costo(costo_hora)
        costo_total += costo
        print(f'[{ot.id_ot}] {ot.tipo_ot():<25} -> Costo: USD {costo:.2f}')

    print('-'*50)
    print(f'COSTO TOTAL ESTIMADO DEL DÍA: USD {costo_total:.2f}')

    iteraciones = 1000
    horas_capacidad = cuadrilla_A.capacidad_diaria_horas
    horas_estimadas_asignadas = cuadrilla_A.horas_asignadas()

    resultados_duracion_total = []
    for _ in range(iteraciones):
        duracion_dia = 0
        for ot in cuadrilla_A.ordenes_asignadas:
            minimo = ot.duracion_estimada * 0.75
            maximo = ot.duracion_estimada * 1.50
            moda = ot.duracion_estimada
            duracion_real = np.random.triangular(minimo, moda, maximo)
            duracion_dia += duracion_real
        resultados_duracion_total.append(duracion_dia)

    resultados_duracion_total = np.array(resultados_duracion_total)
    prob_incumplimiento = np.mean(resultados_duracion_total > horas_capacidad) * 100

    print(f'\n📊 RESULTADOS MONTECARLO ({iteraciones} iteraciones):')
    print(f'   Horas estimadas planificadas: {horas_estimadas_asignadas:.1f}h')
    print(f'   Horas reales promedio     : {np.mean(resultados_duracion_total):.1f}h')
    print(f'   Probabilidad de requerir horas extra: {prob_incumplimiento:.1f}%')
    print(f'   Horas máximas en peor escenario: {np.max(resultados_duracion_total):.1f}h')
