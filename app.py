import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from db_config import get_connection
import openai

# Configurer ta clé OpenAI
openai.api_key = "TA_CLE_API"

# Fonction : Générer du SQL à partir d'une question
def generate_sql(question, schema_info):
    prompt = f"""
    Tu es un assistant SQL. 
    Voici le schéma de la base de données :
    {schema_info}

    Question utilisateur : "{question}"
    Donne uniquement une requête SQL valide (sans explication).
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    sql_query = response.choices[0].message["content"].strip()
    return sql_query

# Fonction : Exécuter la requête SQL
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

# Fonction : Visualisation intelligente
def smart_visualization(df):
    if df is None or df.empty or len(df.columns) < 2:
        st.info("Pas de visualisation adaptée.")
        return

    x_col, y_col = df.columns[0], df.columns[1]

    try:
        fig, ax = plt.subplots()

        # Cas 1 : si la 1ère colonne ressemble à une date → courbe
        if pd.api.types.is_datetime64_any_dtype(df[x_col]) or "date" in x_col.lower():
            df[x_col] = pd.to_datetime(df[x_col], errors="coerce")
            df.plot(x=x_col, y=y_col, kind="line", marker="o", ax=ax)
            plt.title(f"Évolution de {y_col} par {x_col}")
        
        # Cas 2 : si la 1ère colonne est catégorielle → bar chart
        elif pd.api.types.is_string_dtype(df[x_col]) or df[x_col].nunique() < 20:
            df.plot(x=x_col, y=y_col, kind="bar", ax=ax, legend=False)
            plt.title(f"Comparaison de {y_col} par {x_col}")
            plt.xticks(rotation=45)
        
        # Cas 3 : si c’est des valeurs numériques → scatter plot
        elif pd.api.types.is_numeric_dtype(df[x_col]):
            df.plot(x=x_col, y=y_col, kind="scatter", ax=ax)
            plt.title(f"Relation entre {x_col} et {y_col}")
        
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Impossible de tracer un graphique automatiquement : {e}")

# Interface Streamlit
st.title("🤖 SQL Copilot")
st.write("Pose une question en langage naturel et je génère la requête SQL.")

schema_info = """
Table: customers(id, name, country)
Table: orders(id, customer_id, amount, order_date)
"""

question = st.text_input("Ta question :", placeholder="Ex: Montre-moi le chiffre d’affaires par mois en 2024")

if st.button("Générer et exécuter"):
    if question:
        sql_query = generate_sql(question, schema_info)
        st.code(sql_query, language="sql")

        df = run_query(sql_query)
        if df is not None and not df.empty:
            st.dataframe(df, use_container_width=True)
            smart_visualization(df)
        else:
            st.error("Erreur lors de l'exécution de la requête ou pas de résultats.")
