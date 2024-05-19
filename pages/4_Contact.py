import email
from send_email import send_email
import streamlit as st

from send_email import send_email

st.set_page_config(layout="wide")

st.title("Contact Me")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Email address", placeholder="Enter your email address")
    reason = st.text_input("Reason For Contact", placeholder="Enter your reason for contacting me")
    raw_message = st.text_area("Message", placeholder="Enter your detail message")
    message = f"""\
Subject: {reason}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        if not user_email:
            st.warning("Please enter your email address.")
        elif not reason:
            st.warning("Please enter your reason for contacting.")
        elif not raw_message:
            st.warning("Please enter your message.")
        else:
            send_email(message)
            st.info("Your email has been sent sucessfully.")