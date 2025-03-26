import os

def create_project_structure():
    project_files = [
        "app.py",
        "config.py",
        "models/__init__.py",
        "models/appliance.py",
        "models/problem.py",
        "routes/__init__.py",
        "routes/main.py",
        "services/__init__.py",
        "services/ai_service.py",
        "templates/index.html",
        "static/css/style.css",
        "static/js/script.js",
        "utils/__init__.py",
        "utils/helpers.py",
    ]
    
    for file_path in project_files:
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(file_path, "w") as f:
            f.write("""# This is a placeholder file for {}""".format(file_path))
    
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
