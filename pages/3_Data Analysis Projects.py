import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Data Analysis Projects")

df = pd.read_csv("data-dataA.csv", sep=";")

#list_part1 = df[:len(df)//2]
#list_part2 = df[len(df)//2:]

col_data1, col_data2 = st.columns(2, gap="medium")

with col_data1:
    with st.container(border=True):
        for index, row in df[:len(df)//2].iterrows():
            st.subheader(row["title"])
            st.image("images/" + row["image"])
            cat = f"Category: {row['category']}"
            st.write(cat)
            with st.expander("Project Information"):
                st.write(row["description"])
            st.write(f"[Source Code]({row['url']})")    
            st.divider()
        
        
with col_data2:
    with st.container(border=True):
        for index, row in df[len(df)//2:].iterrows():
            st.subheader(row["title"])
            st.image("images/" + row["image"])
            cat = f"Category: {row['category']}"
            st.write(cat)
            with st.expander("Project Information"):
                st.write(row["description"])
            st.write(f"[Source Code]({row['url']})")  
            st.divider()