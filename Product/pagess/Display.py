import streamlit as st
from SQL import SMTT, DBB

SMT = SMTT()
DB = DBB()

st.set_page_config(
    page_title="Product Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Display")    
SMT.execute('Select * from products')
Record = SMT.fetchall()
DB.close()
if Record :
    st.dataframe(Record)
else :
    st.error("Record Not Found")