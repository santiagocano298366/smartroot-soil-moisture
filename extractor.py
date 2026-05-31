import json, glob, os
with open('notebooks_source.py', 'w', encoding='utf-8') as out:
    for f in glob.glob('g:/Mi unidad/DOCUMENTOS/UNIVERSIDAD/POSGRADO/2026-1/FUNDAMENTOS DE PROGRAMACIÓN CIENTÍFICA/CLASES/PROYECTO_FINAL/notebooks/*.ipynb'):
        out.write(f'\n--- {os.path.basename(f)} ---\n')
        cells = json.load(open(f, encoding='utf-8')).get('cells', [])
        for cell in cells:
            if cell.get('cell_type') == 'code':
                out.write(''.join(cell.get('source', [])))
                out.write('\n')
