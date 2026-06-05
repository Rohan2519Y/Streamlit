import streamlit as st
from SQL import SMTT, DBB

SMT = SMTT()
DB = DBB()

st.set_page_config(
    page_title="Product Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Delete Data")
ProductId = st.text_input("Enter Product Id You Want to Delete")
if st.button("Fetch Data") :
    SMT.execute(f'Select * from products where ProductId = "{ProductId}"')
    Record = SMT.fetchone()
    if Record :
        st.session_state.Show = True
        st.session_state.ProductId = ProductId
    else :
        st.info("Record Not Found")
        
if st.session_state.get("Show", False) :        
    st.write("Do You Want to Delete")
    if st.button("Yes"):
        try :
            SMT.execute(f'Delete from products where ProductId = "{st.session_state.ProductId}"')
            DB.commit()
            st.success("Record Deleted Successfully")
            st.session_state.Show = False
        except Exception as E :
            st.error(E)
        finally :
            DB.close()
    elif st.button("No") :
        st.info("Delete Cancel")