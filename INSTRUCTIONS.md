# How to Run SpamShield AI in Visual Studio Code

This guide will help you run the project using Visual Studio Code (VS Code).

## Prerequisites

Ensure you have the following installed on your computer:
1.  **Visual Studio Code**: [Download Here](https://code.visualstudio.com/)
2.  **Node.js** (for the frontend): [Download Here](https://nodejs.org/)
3.  **Python** (for the backend): [Download Here](https://www.python.org/)

## Step-by-Step Guide

### 1. Open the Project
1.  Launch **Visual Studio Code**.
2.  Go to **File** > **Open Folder...**
3.  Select the folder where you extracted the project (e.g., `SpamShield_Project`).

### 2. Setup the Backend (Python)
1.  Open a new terminal in VS Code: **Terminal** > **New Terminal**.
2.  Navigate to the backend folder:
    ```powershell
    cd backend
    ```
3.  (Optional but recommended) Create a virtual environment:
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  Install Python dependencies:
    ```powershell
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, basic requirements are: `flask flask-cors scikit-learn pandas numpy nltk`)*
5.  Start the Backend Server:
    ```powershell
    python app.py
    ```
    You should see `Running on http://127.0.0.1:5000`.

### 3. Setup the Frontend (React)
1.  Open a **second** terminal (Click the `+` icon in the terminal panel or Split Terminal).
2.  Navigate to the frontend folder:
    ```powershell
    cd frontend
    ```
3.  Install Node dependencies (first time only):
    ```powershell
    npm install
    ```
4.  Start the Frontend:
    ```powershell
    npm run dev
    ```
    You should see `Local: http://localhost:5173/`.

### 4. Use the Application
1.  Ctrl+Click the link `http://localhost:5173/` in the terminal, or open your browser and go to that address.
2.  Use the **"Upload New Dataset (JSON)"** button to load your `sample_dataset.json`.
3.  Click **"Detect Fake Accounts"**.

## Troubleshooting
*   **"pip is not recognized"**: Ensure Python is added to your system PATH.
*   **"npm is not recognized"**: Ensure Node.js is installed.
*   **Backend errors**: Make sure you installed simple-elm or removed the ELM reference if you don't have the specific library (the provided code handles generic ML).
