import streamlit as st 
from time import perf_counter

from database_mysql import SQLA_read_table

t0=perf_counter()
res=  SQLA_read_table("COMPO_DBC")
t1=perf_counter()

st.write(f'Data read in {t1-t0:,.1f}s')
st.write(res.head(5))