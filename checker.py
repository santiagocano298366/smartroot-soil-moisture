import json, glob, os

files = glob.glob('g:/Mi unidad/DOCUMENTOS/UNIVERSIDAD/POSGRADO/2026-1/FUNDAMENTOS DE PROGRAMACIÓN CIENTÍFICA/CLASES/PROYECTO_FINAL/notebooks/*.ipynb')

for f in files:
    print(f"\n--- {os.path.basename(f)} ---")
    with open(f, encoding='utf-8') as file:
        data = json.load(file)
        text = ''
        for cell in data.get('cells', []):
            if cell.get('cell_type') in ['code', 'markdown']:
                text += ''.join(cell.get('source', [])) + '\n'
        
        text_lower = text.lower()
        print(f"  - Funciones ('def '): {'Si' if 'def ' in text_lower else 'No'}")
        print(f"  - Clases ('class '): {'Si' if 'class ' in text_lower else 'No'}")
        print(f"  - Comprensiones: {'Si' if 'comprehension' in text_lower or 'comprensión' in text_lower or 'comprension' in text_lower else 'No'}")
        print(f"  - Montecarlo/Simulación: {'Si' if 'montecarlo' in text_lower or 'simulación' in text_lower or 'simulacion' in text_lower else 'No'}")
        print(f"  - Indicadores: {'Si' if 'indicador' in text_lower or 'kpi' in text_lower else 'No'}")
        print(f"  - Tablero/Gráficos: {'Si' if 'plt.' in text_lower or 'sns.' in text_lower or 'tablero' in text_lower else 'No'}")
