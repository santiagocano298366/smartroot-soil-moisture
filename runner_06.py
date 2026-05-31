import json
import os
import subprocess

nb_path = 'notebooks/06_ordenes_trabajo_mantenimiento.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

codigo = "import matplotlib\nmatplotlib.use('Agg')\n"
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        source = "".join(cell.get('source', []))
        if 'plt.show()' in source and 'savefig' not in source:
            source = source.replace('plt.show()', "plt.savefig('outputs/figuras/06_montecarlo_ans.png', bbox_inches='tight', dpi=150)\nplt.show()")
        codigo += source + "\n\n"

# Asegurar directorios
os.makedirs('outputs', exist_ok=True)
os.makedirs('outputs/figuras', exist_ok=True)

with open('temp_run.py', 'w', encoding='utf-8') as f:
    f.write(codigo)

# Ejecutar y capturar bytes
print("Ejecutando temp_run.py...")
res = subprocess.run(['python', 'temp_run.py'], capture_output=True)

# Decodificar con fallback
out_str = res.stdout.decode('utf-8', errors='replace') if res.stdout else ''
err_str = res.stderr.decode('utf-8', errors='replace') if res.stderr else ''

with open('outputs/06_resultados_ejecucion.txt', 'w', encoding='utf-8') as f:
    f.write("=== RESULTADOS DE EJECUCIÓN DEL NOTEBOOK 06 ===\n\n")
    f.write(out_str)
    if err_str:
        f.write("\n\n=== ERRORES ===\n")
        f.write(err_str)

if os.path.exists('temp_run.py'):
    os.remove('temp_run.py')

print("Ejecución completada. Resultados guardados en outputs/06_resultados_ejecucion.txt")
