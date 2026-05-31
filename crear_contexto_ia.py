import os
import json
import glob

# Rutas
base_dir = r"g:\Mi unidad\DOCUMENTOS\UNIVERSIDAD\POSGRADO\2026-1\FUNDAMENTOS DE PROGRAMACIÓN CIENTÍFICA\CLASES\PROYECTO_FINAL"
nb_dir = os.path.join(base_dir, "notebooks")
outputs_dir = os.path.join(base_dir, "Outputs")
tablas_dir = os.path.join(outputs_dir, "tablas")
out_file = os.path.join(base_dir, "contexto_total_proyecto.md")

with open(out_file, "w", encoding="utf-8") as out:
    out.write("# CONTEXTO TOTAL DEL PROYECTO\n\n")
    out.write("Este documento fue generado para proveer todo el contexto (código, celdas, resultados, csv) a un LLM.\n\n")

    # 1. Requisitos
    out.write("## REQUISITOS DEL PROYECTO\n")
    req_file = os.path.join(base_dir, "requisitos.md")
    if os.path.exists(req_file):
        with open(req_file, "r", encoding="utf-8", errors="ignore") as f:
            out.write(f.read() + "\n\n")
    else:
        out.write("No se pudo leer requisitos.md como texto plano directamente en este script.\n\n")

    # 2. NOTEBOOKS
    out.write("## NOTEBOOKS (CÓDIGO Y RESULTADOS)\n")
    for nb_path in sorted(glob.glob(os.path.join(nb_dir, "*.ipynb"))):
        out.write(f"\n{'='*60}\n### Notebook: {os.path.basename(nb_path)}\n{'='*60}\n")
        try:
            with open(nb_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            for i, cell in enumerate(data.get("cells", [])):
                cell_type = cell.get("cell_type", "")
                source = "".join(cell.get("source", []))
                
                if cell_type == "markdown":
                    out.write(f"\n--- [Celda {i+1} : MARKDOWN] ---\n")
                    out.write(source + "\n")
                elif cell_type == "code":
                    out.write(f"\n--- [Celda {i+1} : CODE] ---\n")
                    out.write(source + "\n")
                    
                    # Tratar de extraer outputs de texto de la celda de codigo
                    outputs = cell.get("outputs", [])
                    if outputs:
                        out.write("\n>>> RESULTADO DE EJECUCIÓN (OUTPUT):\n")
                        for o in outputs:
                            if o.get("output_type") == "stream":
                                out.write("".join(o.get("text", [])))
                            elif o.get("output_type") == "execute_result" or o.get("output_type") == "display_data":
                                data_out = o.get("data", {})
                                if "text/plain" in data_out:
                                    out.write("".join(data_out["text/plain"]))
                        out.write("\n")
        except Exception as e:
            out.write(f"Error leyendo {nb_path}: {e}\n")

    # 3. CSVs Y RESULTADOS DE TEXTO
    out.write("\n## TABLAS CSV Y RESULTADOS FINALES EN OUTPUTS\n")
    
    # 3.1 Resultados txt
    res_txt = os.path.join(outputs_dir, "06_resultados_ejecucion.txt")
    if os.path.exists(res_txt):
        out.write("\n### Archivo: 06_resultados_ejecucion.txt\n")
        with open(res_txt, "r", encoding="utf-8", errors="ignore") as f:
            out.write(f.read() + "\n")
            
    # 3.2 Tablas csv
    for csv_path in sorted(glob.glob(os.path.join(tablas_dir, "*.csv"))):
        out.write(f"\n### Tabla: {os.path.basename(csv_path)}\n")
        try:
            with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
                out.write(f.read() + "\n")
        except Exception as e:
            pass

print(f"Archivo generado exitosamente en: {out_file}")
