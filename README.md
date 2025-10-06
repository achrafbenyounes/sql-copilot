# SQL Copilot 🤖

**SQL Copilot** is an intelligent assistant that generates SQL queries from natural language questions and visualizes the results automatically. Built with Python, Streamlit, and OpenAI’s GPT, this project demonstrates the power of **Generative AI applied to Data**.  

---

## Features 🚀

- Convert natural language questions into SQL queries automatically.
- Execute queries on a database (SQLite for MVP).
- Display results in a table.
- Automatic visualization:
  - Line chart for date/time data
  - Bar chart for categorical data
  - Scatter plot for numeric relationships
- Simple and interactive web interface via **Streamlit**.

---

## Demo 🎬

1. Ask: `"Show total sales per month in 2024"`  
2. SQL Copilot generates the SQL query.  
3. The query executes and results are displayed as a table + chart automatically.

---

## Tech Stack 🛠️

- **Python**  
- **Streamlit** – for the web interface  
- **OpenAI API (GPT-3.5 / GPT-4)** – for SQL generation  
- **SQLite** – database for testing  
- **Matplotlib / Pandas** – for data handling and visualization  

---

## Installation ⚡

1. Clone the repository:  
```bash

git clone https://github.com/achrafbenyounes/sql-copilot.git
cd sql-copilot

2. Install dependencies:

pip install -r requirements.txt

3. Create the database from the sample data from cmd or bash command:

sqlite3 sales.db < sample_data.sql

4. Set your Claude API key:

Configuration de la variable d’environnement CLAUDE_API_KEY (Windows / PowerShell)
Pour que l’application puisse accéder à l’API Claude AI, vous devez définir la clé API dans une variable d’environnement nommée CLAUDE_API_KEY.

🧭 Étapes à suivre
1️⃣ Ouvrir PowerShell

Cliquez sur Démarrer → tapez PowerShell → ouvrez Windows PowerShell (pas besoin de mode administrateur).

2️⃣ Créer la variable d’environnement (permanente)

Dans PowerShell, exécutez :

setx CLAUDE_API_KEY "votre_cle_claude_ici"

Exemple :

setx CLAUDE_API_KEY "sk-ant-api03-XXXXXXXXXXXXXXXXXXXXXXXX"

🟢 Vous devriez voir le message :

RÉUSSITE : la valeur spécifiée a été enregistrée.

3️⃣ Redémarrer PowerShell (ou VS Code)

Fermez la fenêtre PowerShell, puis rouvrez-en une nouvelle.
Vérifiez que la clé est bien enregistrée :

echo $Env:CLAUDE_API_KEY

Si votre clé s’affiche → tout est bon ✅

5. Run the app:

streamlit run app.py

Usage 💡

Type your question in natural language in the Streamlit input box.

Click “Generate and Execute”.

View the generated SQL query, table results, and visualization automatically.

Future Improvements 🔮

Support for more database types (PostgreSQL, MySQL).

Enhanced visualization selection (pie charts, multi-series graphs).

Authentication for private deployments.

Deploy as a cloud web app for wider access.

Contributing 🤝

Contributions are welcome!

Fork the repository

Create a feature branch

Submit a pull request

License 📄

No-Sell License (Simple Version)

Copyright (c) [2025] [Achraf BEN YOUNES]

You are free to use, copy, modify, and share this software **for personal or educational purposes only**.  
You **may not sell, license, or use this software for commercial purposes** without my permission.

This software is provided "as is", without warranty of any kind.


Made with ❤️ by Achraf BEN YOUNES
