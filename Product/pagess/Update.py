import streamlit as st
from SQL import SMTT, DBB

SMT = SMTT()
DB = DBB()

st.set_page_config(
    page_title="Product Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Update Data")
ProductId = st.text_input("Enter Product Id You Want to Update")
Fetch = st.button("Fetch Data")

if Fetch :
    SMT.execute(f'Select * from products where ProductId = "{ProductId}"')
    Record = SMT.fetchone()

    if Record :
        st.session_state.Show = True
        st.session_state.Record = Record
        st.session_state.ProductId = ProductId

    else :
        st.success("Record Not Found")

if st.session_state.get("Show", False) :
    Record = st.session_state.Record
    ProductName = st.text_input("Enter Product Name", value = Record['ProductName'])
    QuantityPerUnit = st.text_input("Enter Quantity Per Unit", value = Record['QuantityPerUnit'])
    UnitPrice = st.text_input("Enter Unit Price", value = Record['UnitPrice'])
    UnitInStock = st.text_input("Enter Unit In Stock", value = Record['UnitInStock'])
    UnitsOnOrder = st.text_input("Enter Units on Order", value = Record['UnitsOnOrder'])
    ReorderLevel = st.text_input("Enter Reorder Level", value = Record['ReorderLevel'])
    Discountinued = st.text_input("Enter Discountinued", value = Record['Discountinued'])
    MFG = st.date_input("Enter MFG", value = Record['MFG'])

    if  st.button("Submit") :
        try :
            Q = f'update products set ProductName = "{ProductName}", QuantityPerUnit = "{QuantityPerUnit}", UnitPrice = "{UnitPrice}", UnitInStock = "{UnitInStock}", UnitsOnOrder = "{UnitsOnOrder}", ReorderLevel = "{ReorderLevel}", Discountinued = "{Discountinued}", MFG = "{MFG}" where ProductId = "{st.session_state.ProductId}"'
            SMT.execute(Q)
            DB.commit()
            st.success("Record Updated Successfully")
            st.session_state.Show = False
    
        except Exception as E :
            st.error(E)