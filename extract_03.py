import json
with open('POO_codigo.py', 'w', encoding='utf-8') as out:
    cells = json.load(open('notebooks/03_POO_indicadores.ipynb', encoding='utf-8')).get('cells', [])
    for c in cells:
        if c.get('cell_type') == 'code':
            out.write(''.join(c.get('source', [])))
            out.write('\n')
