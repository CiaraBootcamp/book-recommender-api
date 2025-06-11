import json
import os

# Ruta del directorio donde están los archivos
base_path = "./"
output_file = "books_all_335.json"

# Lista de archivos por orden
input_files = [
    "books_block_1.json",
    "books_block_2.json",
    "books_block_3.json",
    "books_block_4.json",
    "books_block_5.json",
    "books_block_6.json",
    "books_block_7.json"
]

# Lista donde se irán acumulando todos los libros
all_books = []

# Leer y agregar cada archivo
for file_name in input_files:
    file_path = os.path.join(base_path, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_books.extend(data)

# Guardar el archivo unificado
with open(os.path.join(base_path, output_file), "w", encoding="utf-8") as f_out:
    json.dump(all_books, f_out, ensure_ascii=False, indent=2)

print(f"✅ Todos los libros se han unido correctamente en '{output_file}'")
