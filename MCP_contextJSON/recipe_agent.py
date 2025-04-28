import streamlit as st
import pandas as pd
import json
from fuzzywuzzy import process

# Load recipe data from CSV
df = pd.read_csv("recipes.csv")
dish_names = df['Dish Name'].tolist()

st.title("🍛 Recipe Agent")

# User input
user_input = st.text_input("Enter the dish name", key="dish_input")

if st.button("Get Recipe") and user_input:
    best_match, score = process.extractOne(user_input, dish_names)

    if score >= 70:
        # Fetch recipe row
        recipe_row = df[df["Dish Name"] == best_match].iloc[0]

        # Display ingredients
        ingredients_str = recipe_row["Ingredients"]
        ingredients = [item.strip() for item in ingredients_str.split(",")]
        st.subheader(f"Ingredients for {best_match}:")
        for ing in ingredients:
            st.write(f"- {ing}")

        # Display instructions
        instructions = recipe_row["Instructions"]
        st.subheader(" How to Make It:")
        st.write(instructions)

        # Save context for Shopping Agent
        with open("context.json", "w") as f:
            json.dump({
                "dish_name": best_match,
                "ingredients": ingredients
            }, f)

        st.success(" Recipe saved for Shopping Assistant!")

    else:
        st.error(" Recipe not found. Please try another dish name.")

# Reset button
if st.button("Reset Search"):
    st.experimental_rerun()
