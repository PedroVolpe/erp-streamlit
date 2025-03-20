import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from faker import Faker

# Interface Streamlit
def main():
    st.subheader("Distribuição das Contas a Pagar por Fornecedor")
    
    conn = sqlite3.connect("erp_finance.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    df = pd.read_sql_query("SELECT fornecedor, SUM(valor) as total_valor FROM contas_pagar GROUP BY fornecedor ORDER BY total_valor DESC", conn)
    
    df_80 = df.nlargest(80, 'total_valor')

    fig = px.pie(df_80, names='fornecedor', values='total_valor')
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()