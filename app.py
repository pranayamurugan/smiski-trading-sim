import streamlit as st 
import pandas as pd
from market import generate_market_data
import time
st.write("hello")

if ('market_open' not in st.session_state): 
        st.session_state.market_open = False
        

st.toggle("market open?", key= "market_open") 


while (st.session_state.market_open):
    generate_market_data()  
    time.sleep(5)

st.write("⏸️ Market is PAUSED")

