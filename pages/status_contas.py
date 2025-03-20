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

    st.subheader("Status das Contas a Pagar e a Receber")

    df_receber = pd.read_sql_query("SELECT status, SUM(valor) as total_valor FROM contas_receber GROUP BY status", conn)

    df_pagar = pd.read_sql_query("SELECT status, SUM(valor) as total_valor FROM contas_pagar GROUP BY status", conn)
         
    df_pagar['tipo'] = 'Contas a Pagar'
    df_receber['tipo'] = 'Contas a Receber'
        
    df_status = pd.concat([df_pagar, df_receber])

    fig = px.bar(df_status, x='tipo', y='total_valor', color='status', labels={'total_valor': 'Valor Total', 'status': 'Status'},barmode='group')
    
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()