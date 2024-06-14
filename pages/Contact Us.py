import streamlit as st
from send_email import send_email


st.header("Contact Us")
with st.form("key=email_form"):
    user_email = st.text_input("Enter your email address")
    topic = st.selectbox(
        "Please select item you want to discuss",
        ("Select Item from list", "Job Enquiries", "Project Proposals", "Other"))
    raw_message = st.text_area("Please enter your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Send")
    print(button)
    if button:
        send_email(message)
        st.info("Your email is sent successfully.")



