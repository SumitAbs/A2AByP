import streamlit as st
import pandas as pd
from fuzzywuzzy import process

# Load the dataset
df = pd.read_csv("veg_recipes.csv")

st.title("🍽️ AI Recipe Agent")

# Initialize session state
if "dish_input" not in st.session_state:
    st.session_state.dish_input = ""

# Reset button (comes before text_input)
if st.button(" Reset"):
    st.session_state.dish_input = ""
    st.rerun()  #  This is the correct method now

# Input field
dish_name = st.text_input("Enter the name of the dish:", key="dish_input")

# Recipe search logic
if dish_name:
    matches = process.extractOne(dish_name, df["Dish Name"])
    if matches and matches[1] > 60:
        result = df[df["Dish Name"] == matches[0]].iloc[0]
        st.success(f"**Dish:** {result['Dish Name']}")
        st.write(f"**Ingredients:** {result['Ingredients']}")
        st.write(f"**Instructions:** {result['Instructions']}")
    else:
        st.warning(" Sorry, no matching recipe found,we will update soon.")
