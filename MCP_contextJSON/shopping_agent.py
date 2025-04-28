import streamlit as st
import json

st.title("🛍️ Shopping Agent")

try:
    with open("context.json", "r") as f:
        context = json.load(f)
except FileNotFoundError:
    context = {"dish_name": "", "ingredients": []}

if context["dish_name"]:
    st.write(f"### Suggested Ingredients for **{context['dish_name']}**:")
    for item in context["ingredients"]:
        st.write(f"- {item}")

    if st.button("Order Ingredients"):
        st.success("🛒 Ingredients ordered successfully!")
else:
    st.warning("No recipe selected yet. Go to Recipe Agent first.")
