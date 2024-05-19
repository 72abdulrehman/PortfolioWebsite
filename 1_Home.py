import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1: 
    st.title("")
    st.image("images/20240109_125907 (1).jpg", width=300)
    
with col2:
    st.title("Abdul Rehman")
    st.subheader("Software Engineer")
    
st.divider()

content = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
    It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. 
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages.
    """
st.info(content)

st.divider()

st.title("Portfolio Projects")

col3, col4 = st.columns(2, gap="medium")

with col3:
    st.subheader("Python Projects")
    st.image("images/Python-projects-1.png")
    st.page_link("pages/2_Python Projects.py", label="View Projects")
    
with col4:
    st.subheader("Data Analysis Projects")
    st.image("images/data-visualization-3 (1).png")
    st.page_link("pages/3_Data Analysis Projects.py", label="View Projects")

st.divider()