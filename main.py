import streamlit as st
import pandas

# Set webpage layout to wide.

st.set_page_config(layout="wide")

st.header("Aggarwal Industries")
content = """ We are manufacturer of Plastic bags for POP, Feed, Khal. 
We are located at Hanumangarh Town, Kohla. Rajasthan. 335513 """
st.write(content)
st.subheader("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

# Add content to first column

with col1:
    # Iterate over the first four rows only
    for index, row in df[:4].iterrows():
        # Add members first and last name
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        # Add members role in the company
        st.write(row["role"])
        # Add members images
        st.image("images/" + (row["image"]))
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + (row["image"]))
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + (row["image"]))
