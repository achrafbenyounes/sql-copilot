# SQL Copilot 🤖

**SQL Copilot** is an intelligent assistant that generates SQL queries from natural language questions and visualizes the results automatically. Built with Python, Streamlit, and Claude Sonnet, this project demonstrates the power of **Generative AI applied to Data**.  

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
- **CLAUDE API (Sonnet 4)** – for SQL generation  
- **SQLite** – database for testing  
- **Matplotlib** – for visualization  

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

🔧 Setting the CLAUDE_API_KEY Environment Variable (Windows / PowerShell)

To allow the application to access the Claude AI API, you need to set your API key in an environment variable named CLAUDE_API_KEY.

🧭 Steps to follow

1️⃣ Open PowerShell

Click Start → type PowerShell → open Windows PowerShell (no need for administrator mode).

2️⃣ Create the Environment Variable (Permanent)

In PowerShell, run:

setx CLAUDE_API_KEY "your_claude_api_key_here"

Example:

setx CLAUDE_API_KEY "sk-ant-api03-XXXXXXXXXXXXXXXXXXXXXXXX"

🟢 You should see the message:

SUCCESS: The specified value was saved.

3️⃣ Restart PowerShell (or VS Code)

Close the PowerShell window and open a new one.
Check that the key is correctly set:

echo $Env:CLAUDE_API_KEY

If your key is displayed → everything is good ✅

5. Run the app:

streamlit run app.py

Usage 💡

Type your question in natural language in the Streamlit input box.

Click “Generate and Execute”.

View the generated SQL query, table results, and visualization automatically.

Example of execution :

show me the total amount of all orders by client name

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
