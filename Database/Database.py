import streamlit as st
import pymysql as sql
from streamlit_option_menu import option_menu

st.set_page_config(
    layout='wide',
    page_icon='💻',
    page_title='Database'
)

if 'DB_Connection' not in st.session_state:
    st.session_state["DB_Connection"] = True

if st.session_state.get("DB_Connection", True):
    st.title("Enter SQL Details")
    host = st.text_input("Enter Host", value='localhost')
    port = st.text_input("Enter Port", value=3306)
    username = st.text_input("Enter Username", value='root')
    password = st.text_input("Enter Password", value='1234')

    if st.button("Submit"):
        try:
            DB = sql.connect(
                host=host,
                port=int(port),
                user=username,
                password=password,
                cursorclass=sql.cursors.DictCursor
            )

            SMT = DB.cursor()
            st.success("Connection Established")
            st.session_state.SMT = SMT
            st.session_state.DB = DB
            st.session_state.DB_Connection = False
            st.rerun()

        except Exception as E:
            st.error(E)

def fetchData():
    SMT = st.session_state.get("SMT")
    if st.session_state.get('TableData'):
        try:
            SMT.execute(f"select * from {st.session_state.get('TableData')}")
            Record = SMT.fetchall()
            st.dataframe(Record)

        except Exception as E:
            st.error(E)

def fetchTables():
    SMT = st.session_state.get("SMT")

    if st.session_state.get('Tables'):
        try:
            SMT.execute(f"USE {st.session_state.get('Tables')}")
            SMT.execute("SHOW TABLES")
            Record = SMT.fetchall()
            options = ['Select Table'] + list(
                map(lambda v: v[f"Tables_in_{st.session_state.get('Tables')}"], Record)
            )
            Tables = st.selectbox(
                "Select Table",
                options,
                index=st.session_state.get("TableIndex", 0)
            )
            st.session_state.TableIndex = options.index(Tables)
            if Tables != 'Select Table':
                st.session_state.TableData = Tables
                fetchData()

        except Exception as E:
            st.error(E)

if st.session_state.get("SMT"):
    menu = option_menu(
        menu_title=None,
        options=["Home", "Insert", "Update", "Delete", "Search"],
        icons=["house", "plus-circle", "pencil-square", "trash", "search"],
        orientation = 'horizontal'
    )
    SMT = st.session_state.get("SMT")
    DB = st.session_state.get("DB")
    if menu == 'Home':
        SMT.execute("SHOW DATABASES")
        Record = SMT.fetchall()
        options = ['Select Database'] + list(map(lambda v: v['Database'], Record))
        Database = st.selectbox(
            "Select Database",
            options,
            index=st.session_state.get("DatabaseIndex", 0)
        )
        st.session_state.DatabaseIndex = options.index(Database)
        if Database != 'Select Database':
            st.session_state.Tables = Database
            fetchTables()

    elif menu == 'Insert':
        if 'TableData' in st.session_state:
            st.title(f"Database - {st.session_state.Tables}")
            st.title(f"Table - {st.session_state.TableData}")        
            SMT.execute(f"Describe {st.session_state.TableData}")
            Record = SMT.fetchall()
            L = []
            for i in Record:
                if 'date' in i['Type']:
                    Data = st.date_input(f"{i['Field']}")
                    Data = Data.strftime("%Y-%m-%d")
                else:
                    Data = st.text_input(f"{i['Field']}", value='')
                D = {}
                D[i['Field']] = Data
                L.append(D)
            Q = [list(i)[0] for i in L]
            V = [
                f"'{list(i.values())[0]}'" if isinstance(list(i.values())[0], str)
                else str(list(i.values())[0])
                for i in L
            ]
            query = f"insert into {st.session_state.TableData} values ({', '.join(V)})"
            st.write(query)
            if st.button("Submit"):
                try:
                    SMT.execute(query)
                    if DB:
                        DB.commit()
                    else:
                        st.error("Database connection not found")
                    st.success("Data Submitted Successfully")
                except Exception as E:
                    st.error(E)
        else:
            st.write("Please Select the Table First")

    elif menu == 'Update':
        if 'TableData' in st.session_state:
            st.title(f"Database - {st.session_state.Tables}")
            st.title(f"Table - {st.session_state.TableData}")
        else:
            st.write("Please Select the Table First")

    elif menu == 'Delete':
        if 'TableData' in st.session_state:
            st.title(f"Database - {st.session_state.Tables}")
            st.title(f"Table - {st.session_state.TableData}")
        else:
            st.write("Please Select the Table First")

    elif menu == 'Search':
        if 'TableData' in st.session_state:
            st.title(f"Database - {st.session_state.Tables}")
            st.title(f"Table - {st.session_state.TableData}")
        else:
            st.write("Please Select the Table First")