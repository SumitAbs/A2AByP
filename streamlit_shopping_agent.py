import streamlit as st
import pandas as pd
from fuzzywuzzy import process

# Load recipe data
df = pd.read_csv("recipes.csv")

st.title("🛒 Shopping Assistant")

# User input for dish name
dish_input = st.text_input("Enter the dish name:", key="dish_input")

# Button to generate shopping list
if st.button("Generate Shopping List"):
    # Fuzzy match the dish
    match = process.extractOne(dish_input, df["Dish Name"].tolist())
    
    if match and match[1] >= 70:
        selected_recipe = df[df["Dish Name"] == match[0]].iloc[0]
        st.subheader(f"Ingredients for: {selected_recipe['Dish Name']}")
        
        # Split and display as bullet points
        ingredients = selected_recipe["Ingredients"].split(",")
        for item in ingredients:
            st.markdown(f"- {item.strip()}")

        # Simulated Order Button
        if st.button("🛍️ Place Order"):
            st.success("Order placed successfully! 📦")
    else:
        st.error("Dish not found. Please try a different name.")
