import re
import os

path = r'g:\Mi unidad\DOCUMENTOS\UNIVERSIDAD\POSGRADO\2026-1\FUNDAMENTOS DE PROGRAMACIÓN CIENTÍFICA\CLASES\PROYECTO_FINAL\Informe\main.tex'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix characters
text = text.replace('“', '"').replace('”', '"')
text = text.replace('‘', "'").replace('’', "'")
text = text.replace('—', '---')
text = text.replace('–', '--')
text = text.replace('…', '...')
text = text.replace('\xa0', ' ') # non-breaking space

# Fix image paths
text = text.replace('dashboard_smartroot.png', '../Outputs/figuras/05_tablero_control_completo.png')
text = text.replace('mc_histogramas.png', '../Outputs/figuras/04_mc_histogramas_escenarios.png')
text = text.replace('convergencia_mc.png', '../Outputs/figuras/04_mc_serie_temporal.png')
text = text.replace('correlaciones.png', '../Outputs/figuras/01_correlaciones.png')
text = text.replace('diagrama_flujo.png', '../Outputs/figuras/05_diagrama_flujo.png')

# Fix literate in lstset
if 'literate=' not in text:
    lit_str = "    tabsize=4,\n    literate={á}{{\\'a}}1 {é}{{\\'e}}1 {í}{{\\'i}}1 {ó}{{\\'o}}1 {ú}{{\\'u}}1 {Á}{{\\'A}}1 {É}{{\\'E}}1 {Í}{{\\'I}}1 {Ó}{{\\'O}}1 {Ú}{{\\'U}}1 {ñ}{{\\~n}}1 {Ñ}{{\\~N}}1,\n    frame=single,"
    text = text.replace("    tabsize=4,\n    frame=single,", lit_str)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixes applied.')
