import streamlit as st
import pymysql as sql

try:
    DBS = sql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '1234',
        database = 'my_industry',
        cursorclass = sql.cursors.DictCursor
    )    
    SMTS = DBS.cursor()
except Exception as e:
    st.error(e)

def SMTT() :
    return SMTS

def DBB() :
    return DBS