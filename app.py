import streamlit as st
import cohere

# Set your Cohere API key here
co = cohere.Client("7Inil0a76TZkMeSnu63ZAlW7f7HYQH1Iduuca8Kv")

def generate_recipe(ingredients):
    prompt = f"""
    You are a professional chef. Create a detailed recipe using only the following ingredients:
    {', '.join(ingredients)}.
    
    Include the following sections:
    1. Dish Name
    2. Ingredients List
    3. Instructions
    4. Cooking Time
    5. Serving Size
    
    Make it clear and easy to follow.
    """
    
    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Recipe Generator", page_icon="🍳")
st.title("🍳 AI-Powered Recipe Generator")
st.subheader("Enter ingredients and get a recipe!")

# User input
user_input = st.text_area(
    "Enter ingredients separated by commas:", 
    height=100,
    placeholder="e.g., chicken, rice, broccoli, garlic, soy sauce"
)

if st.button("Generate Recipe", use_container_width=True):
    if user_input.strip() == "":
        st.warning("Please enter at least one ingredient.")
    else:
        ingredients = [item.strip() for item in user_input.split(",") if item.strip()]
        
        # Display the ingredients being used
        st.info(f"Generating recipe for: {', '.join(ingredients)}")
        
        with st.spinner("👩‍🍳 Generating your recipe..."):
            recipe = generate_recipe(ingredients)
            
            if recipe.startswith("Error:"):
                st.error(recipe)
            else:
                st.success("Recipe generated successfully!")
                st.markdown("### Here's Your Recipe:")
                st.markdown(recipe)

# Add footer
st.markdown("---")
st.markdown("Developed by SRINIVAS THOTA")
