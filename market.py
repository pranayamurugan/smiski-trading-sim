import streamlit as st
import random 
import pandas as pd
import os
import datetime 

global last_price 
global df

csv_path = 'data/bubbles.csv'
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path) 
else:
    df = pd.DataFrame(columns=['time', 'price'])
    df.to_csv(csv_path, index=False)

if df.empty: 
    new_row = pd.DataFrame([[datetime.datetime.now(), 11.5]], columns=['time', 'price'])
    df = pd.concat([df, new_row], ignore_index=True)
else:
    last_price = df['price'].iloc[-1]


# want to generate random price changes as a function of time for each model 
# store in csv these data points

print(st.session_state.get("market_open"))
def generate_market_data():
    global df
    if not st.session_state.get("market_open", False):
        return
    change_pct = random.gauss(0, 0.005)  # mean 0%, standard deviation 0.5%
    last_price = (df['price'].iloc[-1] * (1 + change_pct))
    new_row = pd.DataFrame({'time': [datetime.datetime.now()], 'price': [last_price]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(csv_path, index=False) 
    print(last_price)


