import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from faker import Faker

# Interface Streamlit
def main():
    st.title("Fluxo de caixa")
    
    conn = sqlite3.connect("erp_finance.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    df = pd.read_sql_query("SELECT * FROM contas_pagar", conn)

    fig = px.pie(df,)


if __name__ == "__main__":
    main()