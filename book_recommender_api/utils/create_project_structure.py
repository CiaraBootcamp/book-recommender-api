import os

# Estructura del proyecto
structure = {
    "book_recommender_api": {
        "app": [
            "main.py",
            "database.py",
            "models.py",
            "books_controller.py",
            "quiz.py",
            "personality.py",
            "recommender.py",
            "explain.py"
        ],
        "data": [
            "books_all_335.json"
        ],
        "utils": [
            "import_books.py"
        ],
        "": [  # Archivos raíz del proyecto
            "requirements.txt",
            "README.md"
        ]
    }
}

def create_structure(base_path, structure_dict):
    for root_folder, contents in structure_dict.items():
        root_path = os.path.join(base_path, root_folder)
        os.makedirs(root_path, exist_ok=True)
        for subfolder, files in contents.items():
            subfolder_path = os.path.join(root_path, subfolder) if subfolder else root_path
            os.makedirs(subfolder_path, exist_ok=True)
            for filename in files:
                file_path = os.path.join(subfolder_path, filename)
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        f.write(f"# {filename}\n")

if __name__ == "__main__":
    # Cambia esto si quieres que se cree en otra ubicación
    base_directory = os.getcwd()  # Directorio actual
    create_structure(base_directory, structure)
    print(f"\n✅ Estructura creada en: {os.path.join(base_directory, 'book_recommender_api')}")
