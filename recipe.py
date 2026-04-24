# -----------------------
# Exercise Set 6 solution
# -----------------------
recipes = {
    "Pasta": {"spaghetti", "olive oil", "garlic"},
    "Omelette": {"eggs", "milk", "salt"},
    "Pancakes": {"flour", "milk", "egg", "sugar"},
}


# -----------------------
# Step 0 - Core Functions
# -----------------------
def list_recipes():
    for i, name in enumerate(recipes, start=1):
        ingredients = ", ".join(recipes[name])
        print(f"{i}. {name} \t -> \t {ingredients}")


def add_recipe(name):
    ingredients = input("Ingredients (comma-separated, no space): ")
    ingredients = ingredients.split(",")
    recipes[name] = set(ingredients)
    print(f"Added '{name}' with {len(ingredients)} ingredients.")


def save_recipes():
    with open("recipes.txt", "w") as f:
        for name in recipes:
            f.write(name)
            f.write(",")
            for ing in recipes[name]:
                f.write(ing)
                f.write(",")
            f.write("\n")
    print("Successfully saved recipes. Quitting...")


def load_recipes(path="recipes.txt"):
    try:
        with open(path, "r") as f:
            data = f.readlines()
            for recipe in data:
                recipe = recipe.strip().split(",")
                name = recipe[0]
                ingredients = set(recipe[1:-1])
                recipes[name] = ingredients
            print("recipes.txt successfully loaded...")
    except FileNotFoundError:
        print("recipes.txt does not exist. Loading default recipes...")


# -----------------------
# Step 1 - Clean Recipes
# -----------------------
def to_title(s):
    return s.strip().title()


def clean_recipes():
    """Format the ingredients with title case."""
    for name in recipes:
        recipes[name] = set(map(to_title, recipes[name]))
    print("Recipes cleaned! All ingredients are now in title case.\n")


# -----------------------
# Step 2 - Find by Ingredient
# -----------------------
def recipe_uses_ingredient(target):
    def pred(recipe):  # recipe = (name, ingredient_set)
        return target in recipe[1]
    return pred


def find_by_ingredient(ingredient):
    """List all recipes that use a specific ingredient."""
    ingredient = to_title(ingredient)
    search_fn = recipe_uses_ingredient(ingredient)

    matches = list(filter(lambda item: search_fn(item), recipes.items()))

    if not matches:
        print(f"No recipes contain '{ingredient}'.\n")
        return

    print(f"\nRecipes with '{ingredient}':")
    for i, (name, _) in enumerate(matches, start=1):
        print(f"{i}. {name}")
    print()


# -----------------------
# Step 3 - Find Easy Recipes
# -----------------------
def find_easy_recipes(k):
    """List all recipes with at most k ingredients."""
    easy_recipes = [name for name, ingredients in recipes.items() if len(ingredients) <= k]

    if not easy_recipes:
        print(f"No recipes with ≤ {k} ingredients.\n")
        return

    print(f"\nRecipes with ≤ {k} ingredients:")
    for i, name in enumerate(easy_recipes, start=1):
        print(f"{i}. {name}")
    print()


# -----------------------
# Main Menu Loop
# -----------------------
def main():
    load_recipes()
    while True:
        print(f"""
Recipe Manager
[1] List recipes
[2] Add recipe
[3] Find recipe by ingredient
[4] Find easy recipes (≤ K ingredients)
[9] Clean Recipes
[0] Save and Quit""")

        choice = input("> ").strip()

        if choice == "1":
            list_recipes()
        elif choice == "2":
            name = input("Name your recipe: ").strip().title()
            add_recipe(name)
        elif choice == "3":
            ingredient = input("Ingredient to search for: ")
            find_by_ingredient(ingredient)
        elif choice == "4":
            try:
                k = int(input("Max ingredients (Enter a number): ").strip())
                find_easy_recipes(k)
            except ValueError:
                print("Please enter a valid number.\n")
        elif choice == "9":
            clean_recipes()
        elif choice == "0":
            save_recipes()
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
