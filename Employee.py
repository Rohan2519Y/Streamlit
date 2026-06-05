import streamlit as st
import pymysql as sql

try:
    DB = sql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '1234',
        database = 'pythonpractice',
        cursorclass = sql.cursors.DictCursor
    )    
    SMT = DB.cursor()
except Exception as e:
    st.error(e)

st.set_page_config(
    page_title="Employee Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.sidebar.title("Employee")
Menu = st.sidebar.radio(
    "Select Option",
    ['Home', 'Insert', 'Display', 'Update', 'Delete', 'Search']
)

if Menu == 'Home' :
    st.title("Home")
    st.markdown('''
        - Insert
        - Display
        - Update
        - Delete
        - Search
    ''')

elif Menu == 'Insert' :
    st.title("Insert Data")
    employeeid = st.text_input("Enter Employee Id")
    empname = st.text_input("Enter Employee Name")
    city = st.text_input("Enter City")
    if st.button("Submit"):
        try :
            SMT.execute(f"Insert into employees values ({employeeid}, '{empname}', '{city}')")
            DB.commit()
            DB.close()
            st.success("Record Submitted Successfully")
        except Exception as E :
            st.error(E)

elif Menu == 'Display' :
    st.title("Display Data")
    st.title("Display")    
    SMT.execute('Select * from employees')
    Record = SMT.fetchall()
    DB.close()
    if Record :
        st.dataframe(Record)
    else :
        st.error("Record Not Found")

elif Menu == 'Update' :
    st.title("Update Data")

elif Menu == 'Delete' :
    st.title("Delete Data")
    employeeid = st.text_input("Enter Employee Id")
    if st.button("Fetch Record"):
        SMT.execute(f"Select * from employees where employeeid = {employeeid}")
        Record = SMT.fetchone()
        if Record :
            st.session_state.User = True
            st.session_state.employeeid = employeeid
        else :
            st.info("Record Not Found")

    if st.session_state.get('User', False):
        st.write("Do you want to delete")
        if st.button("Yes"):
            SMT.execute(f"Delete from employees where employeeid = {st.session_state.employeeid}")
            DB.commit()
            DB.close()
            st.session_state.User = False
            st.success("Deleted Successfull")
        elif st.button("No") :
            st.info("Cancel")


elif Menu == 'Search' :
    st.title("Search Data")


else :
    st.title("Home")