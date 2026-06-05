import streamlit as st
import pymysql as sql
from streamlit_option_menu import option_menu

try:
    DB = sql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '1234',
        database = 'my_industry',
        cursorclass = sql.cursors.DictCursor
    )    
    SMT = DB.cursor()
except Exception as e:
    st.error(e)

st.set_page_config(
    page_title="Product Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Product")

with st.sidebar:
    menu = option_menu(
        menu_title=None,
        options=["Home", "Display", "Insert", "Update", "Delete", "Search"],
        icons=["house", "table", "plus-circle", "pencil-square", "trash", "search"],
        orientation="vertical"
    )

if menu == "Home":
    st.image("../product.jfif",width = 500)
    st.title("Product Management System")
    st.write("Display Data")
    st.write("Update Data")
    st.write("Delete Data")
    st.write("Search Data")

elif menu == "Display":
    st.title("Display")    
    SMT.execute('Select * from products')
    Record = SMT.fetchall()
    DB.close()
    if Record :
        st.dataframe(Record)
    else :
        st.error("Record Not Found")

elif menu == "Insert" :
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
            st.error(e)
        finally :
            DB.close()

elif menu == "Update" :
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

elif menu == "Delete" :
    st.title("Delete Data")
    ProductId = st.text_input("Enter Product Id You Want to Delete")

    @st.dialog("Do you want to delete")
    def Dialog(Rec):
        st.dataframe(Rec)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                try :
                    SMT.execute(f'Delete from products where ProductId = "{st.session_state.ProductId}"')
                    DB.commit()
                    st.success("Record Deleted Successfully")
                except Exception as E :
                    st.error(E)
                finally :
                    DB.close()
                    st.rerun()
        with col2 :
            if st.button("No") :
                st.info("Delete Cancel")

    if st.button("Fetch Data") :
        SMT.execute(f'Select * from products where ProductId = "{ProductId}"')
        Record = SMT.fetchone()

        if Record :
            st.session_state.ProductId = ProductId
            Dialog(Record)
        else :
            st.info("Record Not Found")

elif menu == "Search" :
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

else :
    st.image("./product.jfif", width = 500)
    st.title("Product Management System")
    st.write("Display Data")
    st.write("Update Data")
    st.write("Delete Data")
    st.write("Search Data")



#####################################################################################################

# st.title("Product Management")
# st.page_link('pages/Display.py')
# st.page_link('pages/Insert.py')
# st.page_link('pages/Update.py')
# st.page_link('pages/Delete.py')
# st.page_link('pages/Search.py')