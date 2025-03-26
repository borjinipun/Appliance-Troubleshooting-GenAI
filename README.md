# Appliance Troubleshooting Web Application - Python/Flask (Gen-AI)

This project provides a starting point for a Gen-AI-powered appliance troubleshooting web application. It uses Flask for the backend and follows a structured project organization.

## Key Components
- **app.py**: Main application entry point.
- **models/**: Data models (Appliance, Problem).
- **routes/**: Flask routes for handling web requests.
- **services/**: Business logic, including the Gen-AI troubleshooting.
- **templates/**: HTML templates for the frontend.
- **static/**: Static files (CSS, JavaScript, etc.).
- **config.py**: Configuration settings.
- **utils.py**: Utility functions.

## Installation & Setup

### Prerequisites
- Install Python (3.7 or later)
- Install Flask:
  ```bash
  pip install Flask
  ```

### Running the Application
1. Create the project structure as shown below.
2. Save the code into the corresponding files.
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Project Structure
```plaintext
app.py        # Main application entry point
config.py     # Configuration settings

models/
    __init__.py
    appliance.py  # Appliance data model
    problem.py    # Problem data model

routes/
    __init__.py
    main.py       # Main routes (index, diagnose)

services/
    __init__.py
    ai_service.py # Gen-AI logic

templates/
    index.html    # Main page

static/
    css/
        style.css
    js/
        script.js

utils/
    __init__.py
    helpers.py    # Utility functions
```

This project is designed to help users troubleshoot appliance issues efficiently with AI-powered diagnostics.
