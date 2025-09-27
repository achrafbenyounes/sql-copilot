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

3. Create the database from the sample data:

sqlite3 sales.db < sample_data.sql

4. Set your OpenAI API key:

export OPENAI_API_KEY="your_api_key_here"

Or replace it directly in app.py (for testing only).

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
