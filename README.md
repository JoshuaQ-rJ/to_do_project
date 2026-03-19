# 📘 Task Manager CLI -- Main Menu Feature

## 🧩 Overview

This branch implements the **main menu structure** of the Task Manager
CLI application.\
It provides the entry point of the system and allows users to navigate
through different features.

------------------------------------------------------------------------

## 🚀 Features

-   Interactive command-line menu\
-   Navigation between system options\
-   Base structure for integration with services\
-   Clean and modular design

------------------------------------------------------------------------

## 📂 Project Structure

This is the current structure of the project:

    project/
    ├─ src/
    │  ├─ main.py        # Application entry point
    │  ├─ menu.py        # Main menu logic
    │  ├─ validations.py # Input validation
    │  ├─ services.py    # Business logic (CRUD)
    │  └─ models.py      # Data structures
    ├─ README.md
    ├─ .gitignore
    └─ requirements.txt

------------------------------------------------------------------------

## 🛠️ Requirements

-   Python **3.14.x**

------------------------------------------------------------------------

## 🧪 Setup

### 1. Clone the repository

``` bash
git clone <repo-url>
cd <repo-name>
```

### 2. Create virtual environment

``` bash
py -3.14 -m venv venv
```

### 3. Activate environment

**Windows:**

``` bash
venv\Scripts\activate
```

**Mac/Linux:**

``` bash
source venv/bin/activate
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run the project

``` bash
python src/main.py
```

------------------------------------------------------------------------

## 🧠 Usage

The main menu allows users to:

-   Create tasks\
-   View tasks\
-   Update task status\
-   Delete tasks\
-   Exit the application

*(Options will be connected to services in other features.)*

------------------------------------------------------------------------

## 🔁 Workflow

    feat/main-menu → Pull Request → develop

------------------------------------------------------------------------

## 👤 Author

-   **Jose Romero** -- Scrum Master / Main Menu

------------------------------------------------------------------------

## 📌 Notes

-   This feature focuses only on the menu structure\
-   Business logic is handled in `services.py`\
-   Input validation is handled in `validations.py`
