import os
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from db_config import get_connection
import anthropic

# Read the Claude API key from the environment variable
claude_api_key = os.getenv("CLAUDE_API_KEY")

if not claude_api_key:
    raise RuntimeError(
        "❌ Claude/Anthropic API key is not defined.\n"
        "👉 Set the CLAUDE_API_KEY environment variable before running the script."
    )

# ✅ Create an Anthropic client with the retrieved key
client = anthropic.Anthropic(api_key=claude_api_key)

# Function: Generate SQL from a user question
def generate_sql(question, schema_info, db_type):
    prompt = f"""
You are a SQL assistant.
Here is the database schema:
{schema_info}

User question: "{question}"

Provide only a valid SQL query (no explanation),
compatible with **{db_type}**.
"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        temperature=0,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    sql_query = response.content[0].text.strip().replace("sql", "").replace("`", "")
    return sql_query

# Function: Execute the SQL query
def run_query(sql_query):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()
        return pd.DataFrame(results, columns=columns)
    except Exception as e:
        return None

# Function: Smart visualization (automatic + manual)
def smart_visualization(df):
    if df is None or df.empty or len(df.columns) < 2:
        st.info("No suitable visualization available.")
        return

    # Ignore "id" columns
    candidate_cols = [c for c in df.columns if not c.lower().endswith("id") and c.lower() != "id"]

    if len(candidate_cols) < 2:
        st.info("Not enough relevant columns for visualization.")
        return

    st.subheader("📊 Visualization Parameters")

    # Use session_state to avoid rerunning everything
    if "x_col" not in st.session_state:
        st.session_state.x_col = "(Auto)"
    if "y_col" not in st.session_state:
        st.session_state.y_col = "(Auto)"

    manual_x = st.selectbox(
        "X Column:",
        ["(Auto)"] + candidate_cols,
        index=(["(Auto)"] + candidate_cols).index(st.session_state.x_col) 
              if st.session_state.x_col in ["(Auto)"] + candidate_cols else 0,
        key="x_col"
    )
    manual_y = st.selectbox(
        "Y Column:",
        ["(Auto)"] + candidate_cols,
        index=(["(Auto)"] + candidate_cols).index(st.session_state.y_col) 
              if st.session_state.y_col in ["(Auto)"] + candidate_cols else 0,
        key="y_col"
    )

    # Determine X
    if manual_x != "(Auto)":
        x_col = manual_x
    else:
        x_col = None
        for col in candidate_cols:
            if pd.api.types.is_datetime64_any_dtype(df[col]) or "date" in col.lower():
                x_col = col
                break
        if x_col is None:
            for col in candidate_cols:
                if pd.api.types.is_string_dtype(df[col]) or df[col].nunique() < 20:
                    x_col = col
                    break
        if x_col is None:
            x_col = candidate_cols[0]

    # Determine Y
    if manual_y != "(Auto)":
        y_col = manual_y
    else:
        y_col = None
        for col in candidate_cols:
            if col != x_col and pd.api.types.is_numeric_dtype(df[col]):
                y_col = col
                break
        if y_col is None:
            y_col = candidate_cols[1]

    # Generate the plot
    try:
        fig, ax = plt.subplots(figsize=(8, 5))

        if pd.api.types.is_datetime64_any_dtype(df[x_col]) or "date" in x_col.lower():
            df[x_col] = pd.to_datetime(df[x_col], errors="coerce")
            df.plot(x=x_col, y=y_col, kind="line", marker="o", ax=ax, color="tab:blue")
            plt.title(f"Evolution of {y_col} over {x_col}", fontsize=14)

        elif pd.api.types.is_string_dtype(df[x_col]) or df[x_col].nunique() < 20:
            df.groupby(x_col)[y_col].sum().plot(kind="bar", ax=ax, color="tab:green")
            plt.title(f"Comparison of {y_col} by {x_col}", fontsize=14)
            plt.xticks(rotation=45, ha="right")

        else:
            df.plot(x=x_col, y=y_col, kind="scatter", ax=ax, color="tab:red")
            plt.title(f"Relationship between {x_col} and {y_col}", fontsize=14)

        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        st.pyplot(fig)

    except Exception as e:
        st.warning(f"Unable to automatically plot the chart: {e}")

# ======================
# Streamlit Interface
# ======================
st.title("🤖 SQL Copilot")
st.write("Ask a natural language question and I will generate the appropriate SQL query for your database.")

# Select database type
db_type = st.selectbox(
    "Choose your database type:",
    ["SQLite", "PostgreSQL", "Oracle", "SQL Server", "MySQL"]
)

schema_info = """
Table: customers(id, name, country)
Table: orders(id, customer_id, amount, order_date)
"""

question = st.text_input("Your question:", placeholder="Ex: Show monthly revenue for 2024")

if st.button("Generate and Execute"):
    if question:
        sql_query = generate_sql(question, schema_info, db_type)
        st.code(sql_query, language="sql")
        st.write(f"🔍 SQL query generated for {db_type}:", sql_query)

        if db_type == "SQLite":
            df = run_query(sql_query)
            if df is not None and not df.empty:
                st.session_state["df"] = df  # Save query results
                st.dataframe(df, use_container_width=True)
            else:
                st.error("Error executing the query or no results returned.")

# Visualization (do not rerun entire page, only if df exists)
if "df" in st.session_state:
    smart_visualization(st.session_state["df"])
