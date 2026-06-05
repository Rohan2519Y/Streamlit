import streamlit as st
from SQL import SMTT, DBB

SMT = SMTT()
DB = DBB()

st.set_page_config(
    page_title="Product Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.set_page_config(
    page_title="Product Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Insert Data")
ProductId = st.text_input("Enter Product Id")
ProductName = st.text_input("Enter Product Name")
QuantityPerUnit = st.text_input("Enter Quantity Per Unit")
UnitPrice = st.text_input("Enter Unit Price")
UnitInStock = st.text_input("Enter Unit In Stock")
UnitsOnOrder = st.text_input("Enter Units on Order")
ReorderLevel = st.text_input("Enter Reorder Level")
Discountinued = st.text_input("Enter Discountinued")
MFG = st.date_input("Enter MFG")
if st.button("Submit") : 
    try :
        SMT.execute(f'insert into products values ("{ProductId}", "{ProductName}", "{QuantityPerUnit}", "{UnitPrice}", "{UnitInStock}", "{UnitsOnOrder}", "{ReorderLevel}", "{Discountinued}", "{MFG}")')
        DB.commit()
        st.success("Record Submitted Successfully")
    except Exception as E :
        st.error(E)
    finally :
        DB.close()