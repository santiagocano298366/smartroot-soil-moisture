<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/LaTeX-47A141?style=for-the-badge&logo=LaTeX&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  
  <h1>🌱 SmartRoot</h1>
  <p><b>Sistema portátil de bajo costo para la estimación espacial y en tiempo real del potencial mátrico del suelo mediante resistividad eléctrica y aprendizaje automático.</b></p>
  <p><i>Proyecto Final - Fundamentos de Programación Científica <br> Maestría en Automatización y Control Industrial</i></p>
</div>

---

## 📖 Descripción del Proyecto

El objetivo principal del proyecto **SmartRoot** es formular una solución tecnológica orientada a la estimación del potencial mátrico del suelo (medida de retención de humedad y disponibilidad para las plantas). Al conectar programación en Python y un modelo orientado a objetos (POO), se busca representar una parcela de monitoreo agrícola, emular un entorno de incertidumbre y proponer un tablero de evaluación de riesgos hídricos (condiciones de estrés o exceso hídrico). 

Este proyecto aplica los conceptos aprendidos en clase de **Fundamentos de Programación Científica** directamente a los datos reales recopilados por un estudio de redes de sensores empíricos y los asocia a una potencial tesis de maestría.

## 🎯 Cumplimiento de Objetivos del Curso

Este repositorio centraliza todo el trabajo requerido, cumpliendo con cada lineamiento técnico solicitado en la rúbrica `requisitos.docx`:

- ✅ **Programación Básica en Python:** Carga de datos, declaraciones de variables, funciones personalizadas, ciclos (`for`, `while`) y condiciones iterativas para imputación de datos. 
- ✅ **Estructuras de Datos y Comprensiones:** Extensa limpieza de series temporales. Aplicación demostrada de *List Comprehension*, *Dictionary Comprehension*, y *Set Comprehension* directamente sobre el conjunto de datos de sensores para filtrados eficientes y evaluación $O(1)$.
- ✅ **Indicadores KPI de Desempeño:** Formulación matemática y programática de indicadores para evaluar la salud del modelo (Tasa de Error MAPE, porcentaje de observaciones en el rango óptimo, etc). Se consolidaron visualmente en un Dashboard y clasificaron a través de una lógica tipo **Semáforo**.
- ✅ **Programación Orientada a Objetos (POO):** Diseño de la clase abstracta `Sensor` y sus especializaciones hijas (`SensorTensiometro`, `SensorResistivo`, `SensorCapacitivo`) mediante polimorfismo y herencia. Inclusión de la clase agregadora `ParcelaExperimental` para la evaluación masiva de hardware sensor simulado.
- ✅ **Simulación de Montecarlo:** Simulación estocástica implementada con NumPy (`numpy.random`), usando distribuciones gaussianas e iteraciones sintéticas para evaluar la probabilidad de riesgo de riego inminente con estimación de **intervalos de confianza del 95%**.
- ✅ **Visualización e Informes:** Tableros de control complejos combinando *Heatmaps*, *Series Temporales*, *Histogramas* y matrices de correlación (Matplotlib y Seaborn).
- ✅ **LaTeX Académico:** Reporte final tipo artículo técnico y Presentación Beamer rediseñados y compilados sin errores de diseño, utilizando entornos lógicos y limpios.

## 📂 Estructura del Repositorio

```text
PROYECTO_FINAL/
├── data/
│   ├── raw/          # Archivos originales (.tab o .xlsx)
│   └── processed/    # Dataset tratado e imputado (.csv)
├── notebooks/        # Núcleo del proyecto
│   ├── 01_EDA.ipynb                   # Análisis exploratorio y limpieza.
│   ├── 02_programacion_basica.ipynb   # Variables, control de flujo y comprensiones.
│   ├── 03_POO_indicadores.ipynb       # Arquitectura de objetos y KPIs con semáforo.
│   ├── 04_simulacion_montecarlo.ipynb # Simulación estocástica y modelo de riesgo.
│   └── 05_tablero_control.ipynb       # Dashboard integral y gráficos.
├── Informe/          # Documento final tipo artículo
│   └── main.pdf      # Entregable escrito principal
├── Presentacion/     # Diapositivas
│   └── sustentacion.pdf # Presentación Beamer optimizada
└── README.md
```

## 🗃️ Dataset de Referencia

El proyecto utiliza un conjunto de datos real tomado de la red PANGAEA.

> Jackisch, C. et al. (2018): *Soil moisture and matric potential – An open field comparison of sensor systems [dataset].* PANGAEA. https://doi.org/10.1594/PANGAEA.892319

*(Nota: Para proteger el repositorio de sobrecarga de archivos masivos, se incluye un archivo de referencia o script de carga).*

## 🚀 Uso Rápido y Ejecución

Para replicar este proyecto en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone <TU_URL_DE_GITHUB_AQUI>
   cd PROYECTO_FINAL
   ```
2. **Entorno Virtual e Instalación (Opcional pero recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # (en Windows: venv\Scripts\activate)
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. **Ejecutar el Setup o Notebooks:**
   Abre Jupyter Notebook (`jupyter notebook`) y ejecuta secuencialmente desde `notebooks/01_EDA.ipynb` hasta el final. Asegúrate de tener los archivos base descargados en la carpeta `data/raw`.

---
*Desarrollado para la presentación y validación del proyecto final universitario.*
