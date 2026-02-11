# SpamShield AI - Project Overview

This document explains exactly how the **SpamShield AI** project works, from the moment you open the website to how it detects fake accounts.

## 1. The Big Picture (Architecture)
The project is split into two main parts that talk to each other:

1.  **Frontend (The Visuals)**: Built with **React** (JavaScript). This is what you see in the browser. It handles buttons, charts, and file uploads.
2.  **Backend (The Brain)**: Built with **Python (Flask)**. This runs the Machine Learning models and processes the data.

```mermaid
graph LR
    A[User Browser] -- Sends Data (JSON/Text) --> B[Frontend (React)]
    B -- API Calls (HTTP POST) --> C[Backend (Python Flask)]
    C -- Feeds Data --> D[ML Service (Scikit-Learn)]
    D -- Returns Predictions --> C
    C -- JSON Response --> B
    B -- Updates UI --> A
```

## 2. Detailed Process Flow

### A. Detecting Fake Accounts (The Main Feature)
1.  **Upload**: You upload a JSON dataset (like `sample_dataset.json`).
    *   *What happens*: The Frontend sends this file to the Backend at `/api/upload`. The Backend saves it to the `uploads/` folder.
2.  **Analysis**: You click "Detect Fake Accounts".
    *   *What happens*: The Backend reads the JSON file. It looks at every user profile in that file.
3.  **The Logic (Rules & ML)**:
    *   **Fake Rule**: It checks if `followers < friends (following)`. If a user follows 1000 people but only has 5 followers, it's flagged as **Fake**.
    *   **Spam AI**: It extracts the *text* of their tweets. It runs this text through a **Naive Bayes Classifier** (a Machine Learning model trained to recognize spam words like "buy now", "click link", etc.).
4.  **Result**: The Backend counts how many are fake/spam and sends the list back. The Frontend displays the summary numbers and fills the "Activity Log".

### B. Live Text Check
1.  **Input**: You type a specific tweet into the text box (e.g., "Win a free iPhone").
2.  **Process**: The Frontend sends just this text to `/api/predict/text`.
3.  **Prediction**: The ML model in `ml_service.py` converts the text into numbers (vectorization) and asks the trained Classifier: "Is this spam?"
4.  **Result**: It returns "Spam" or "Non-Spam".

### C. Manual User Check
1.  **Input**: You manually type "Followers: 10" and "Following: 500".
2.  **Logic**: The system runs the simple rule: `Is Followers < Following?`
3.  **Result**: It tells you if the account looks fake based purely on that ratio.

### D. Model Comparison (The Chart)
1.  **Action**: You click "Run Naive Bayes", "Run SVM", or "Run ELM".
2.  **Training**: The Backend loads the features extracted from your dataset. It splits them into "Training Data" (to teach the model) and "Test Data" (to quiz the model).
3.  **Evaluation**: It trains the chosen algorithm and then tests it. It calculates **Accuracy** (how often it was right).
4.  **Visuals**: The accuracy score is sent to the Frontend, which updates the purple Bar Chart to compare which algorithm is best.

## 3. Key Technologies Used

*   **React (Vite)**: For a fast, modern user interface.
*   **Python Flask**: A lightweight web server to handle requests.
*   **Scikit-Learn**: The library used for the Machine Learning algorithms (Naive Bayes, SVM).
*   **Numpy/Pandas**: Used for data manipulation in Python.
*   **Recharts**: The library used to draw the bar chart in the browser.

## 4. Where is the "AI"?
The AI lives in `backend/ml_service.py`. It uses:
*   **CountVectorizer**: assigning numbers to words (e.g., "free" = 523, "win" = 899).
*   **BernoulliNB**: A probabilistic classifier that calculates the likelihood of a text being spam based on the words it contains.
*   **ELM (Extreme Learning Machine)**: A neural network approach used for high-speed classification (we included a custom implementation for this).
