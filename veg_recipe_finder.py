import pandas as pd

# Load CSV
df = pd.read_csv("veg_recipes.csv")

# Function to get recipe
def get_recipe(dish_name):
    match = df[df['Dish Name'].str.lower() == dish_name.lower()]
    if not match.empty:
        ingredients = match.iloc[0]['Ingredients']
        instructions = match.iloc[0]['Instructions']
        return ingredients, instructions
    else:
        return None, None

# Testing it
if __name__ == "__main__":
    dish = input("Enter dish name: ")
    ingredients, instructions = get_recipe(dish)
    if ingredients:
        print("\nIngredients:\n", ingredients)
        print("\nInstructions:\n", instructions)
    else:
        print("Sorry, recipe not found.")
