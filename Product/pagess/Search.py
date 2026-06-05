import streamlit as st
from SQL import SMTT, DBB

SMT = SMTT()
DB = DBB()

st.set_page_config(
    page_title="Product Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Search Data")
ProductId = st.text_input("Enter Product Id You Want to Search")
if st.button("Fetch Data") :
    SMT.execute(f'Select * from products where ProductId = "{ProductId}"')
    Record = SMT.fetchall()
    if Record :
        st.dataframe(Record)
        st.success("Data Fetched Successfully")
    else :
        st.info("Record Not Found")